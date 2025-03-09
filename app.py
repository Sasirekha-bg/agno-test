from agno.agent import Agent
from agno.tools.github import GithubTools
from agno.models.google import Gemini
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["GITHUB_ACCESS_TOKEN"] = os.getenv("GITHUB_ACCESS_TOKEN")
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    instructions=[
        "Use your tools to answer questions about the repo: agno-agi/agno",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools(search_repositories=True)],
    show_tool_calls=True,
    
)

agent.print_response("can you get me details of readme file in sasirekha-bg/YT-Transcriber repo ", markdown=True)