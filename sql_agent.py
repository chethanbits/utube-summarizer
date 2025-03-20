# sql_agent.py
from sqlalchemy import create_engine, text
from crewai import Agent
from crewai_tools import NL2SQLTool
from config import DB_URI, config, TABLES
from crewai import LLM


class CustomNL2SQLTool(NL2SQLTool):
    """Custom NL2SQL tool that runs MariaDB-compatible queries."""
    max_tables: int = 10  # Define max_tables as a model field with default value
    
    def __init__(self, db_uri=None, max_tables=10):
        super().__init__(db_uri=db_uri or DB_URI)
        self.max_tables = max_tables

    def _fetch_available_tables(self):
        """Return a limited number of tables based on max_tables setting."""
        limited_tables = TABLES[:self.max_tables] if len(TABLES) > self.max_tables else TABLES
        return [{"table_name": table} for table in limited_tables]

    def _fetch_all_available_columns(self, table_name):
        """Fetch column names and data types from MariaDB."""
        try:
            engine = create_engine(self.db_uri)
            with engine.connect() as conn:
                result = conn.execute(text(f"DESCRIBE `{table_name}`"))
                columns = [{"column_name": row[0], "data_type": row[1]} for row in result]
            return columns
        except Exception as e:
            print(f"Error fetching columns for {table_name}: {e}")
            return []

    def execute_query(self, sql_query):
        """Run SQL queries and return the results."""
        print(f"\nExecuting SQL Query:\n{sql_query}\n")

        try:
            engine = create_engine(self.db_uri)
            with engine.connect() as conn:
                result = conn.execute(text(sql_query))
                rows = [dict(row) for row in result]
                
                # Print a sample of results for immediate feedback
                if rows:
                    print(f"Query returned {len(rows)} results. Sample:")
                    for i, row in enumerate(rows[:3]):  # Show first 3 rows
                        print(f"Row {i+1}: {row}")
                    if len(rows) > 3:
                        print("...")
                else:
                    print("Query returned no results")
                    
            return rows
        except Exception as e:
            error_message = f"Error executing query: {str(e)}"
            print(error_message)
            return [{"error": error_message}]

# Create the NL2SQL tool instance
nl2sql_tool = CustomNL2SQLTool(db_uri=DB_URI, max_tables=5)

# Initialize LLM with Azure OpenAI
llm = LLM(
    model="azure/gpt-4o",
    api_version='2024-05-01-preview',
    max_tokens=1000  # Limit response size
)

# Define SQL Agent
sql_agent = Agent(
    role="SQL Query Agent",
    goal="Convert natural language queries into SQL and execute them accurately",
    backstory="""You are an expert SQL developer specializing in MariaDB. 
    You translate natural language requests into optimized SQL queries.
    You understand database schemas and can efficiently retrieve information.""",
    tools=[nl2sql_tool],
    llm=llm,
    verbose=True
)