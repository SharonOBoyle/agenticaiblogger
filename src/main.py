import os
from dotenv import load_dotenv
from crewai import Crew
from agents import BlogArticleAgents
from tasks import BloggingTasks


def main():
    load_dotenv()

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    if not GROQ_API_KEY:
        raise ValueError("Missing Groq AI API key. Make sure GROQ_API_KEY is set in the .env file.")

    agents = BlogArticleAgents()
    tasks = BloggingTasks()

    planner = agents.planner()
    writer = agents.writer()
    editor = agents.editor()

    plan = tasks.plan(planner)
    write = tasks.write(writer)
    edit = tasks.edit(editor)

    
    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan, write, edit],
        verbose=2
    )
    
   
    #logging.basicConfig(level=logging.DEBUG)
    result = crew.kickoff(inputs={"topic": "Artificail Intelligence"})
    if result is None:
        print("No output received from CrewAI.")
    else:
        print(result)


if __name__ == "__main__":
    main()
    