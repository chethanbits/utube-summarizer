from crewai import Agent,LLM

llm = LLM(
    model="azure/gpt-4o",
    api_version='2024-05-01-preview'
)

report_agent = Agent(
    role="Report Generator",
    goal="Analyze retrieved data and generate a report of the recieved data . dont add more summary text only beutify the result.",
    backstory="""You are an experienced data analyst and report writer with expertise in transforming
    complex data into clear, actionable insights.""",
    tools=[],
    allow_delegation=True,
    llm=llm
)
