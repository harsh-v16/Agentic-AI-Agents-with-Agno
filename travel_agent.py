from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=OpenAIResponses(id="gpt-5-mini"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpfull and expert travel agent.",
        add_datetime_to_context=True
        
    )

openai_agent = build_agent()

openai_agent.print_response("Is it safe to travel to UAE today?")