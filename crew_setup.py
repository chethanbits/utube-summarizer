# Updated crew_setup.py
from crewai import Crew
from tasks import create_sql_task, create_report_task
from sql_agent import sql_agent
from report_agent import report_agent

def run_crew(nl_query):
    # Create tasks with the natural language query
    sql_task = create_sql_task(nl_query)
    report_task = create_report_task()
    
    # Create Crew with agents and tasks
    crew = Crew(
        agents=[sql_agent, report_agent], 
        tasks=[sql_task, report_task],
        verbose=True
    )
    
    result = crew.kickoff()
    return result