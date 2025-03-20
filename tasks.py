# tasks.py
from crewai import Task
from sql_agent import sql_agent, nl2sql_tool
from report_agent import report_agent

# Define the SQL retrieval task
def create_sql_task(nl_query):
    return Task(
        description=f"Convert and execute the following natural language query: '{nl_query}'.",
        agent=sql_agent,
        expected_output="A JSON response containing structured data retrieved from the database."
    )

# Define the report generation task
def create_report_task():
    return Task(
        description="Generate a comprehensive report based on the SQL results from the previous task",
        agent=report_agent,
        expected_output="A detailed analysis of the SQL query results with key insights."
    )