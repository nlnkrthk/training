from crewai import Agent, Task, Crew


# 1. Create an agent
writer = Agent(
    role="Technical Writer",
    goal="Explain technical concepts in a simple way",
    backstory="You are an experienced technical teacher."
)

reviewer = Agent(
    role="Review Manager",
    goal="Ensure the quality and accuracy of technical explanations",
    backstory="You are a meticulous editor with a keen eye for detail."
)


# 2. Create a task
write_task = Task(
    description="Explain what an API is to a beginner.",
    expected_output="A simple explanation of an API with one example.",
    agent=writer
)

review_task = Task(
    description="""
    Review the explanation created by the writer.
    Check whether it is accurate, simple and easy to understand.
    Correct it if necessary.
    """,
    
    expected_output="A corrected and beginner-friendly explanation.",
    
    agent=reviewer
)

# 3. Create a crew
crew = Crew(
    agents=[writer, reviewer],
    tasks=[write_task, review_task]
    process = Process.sequential
)


# 4. Start the crew
result = crew.kickoff()


# 5. Print the result
print(result)