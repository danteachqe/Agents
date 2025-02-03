import os
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Retrieve the API key from the system environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("The 'OPENAI_API_KEY' environment variable is not set.")

# Define a tool
async def get_weather(city: str) -> str:
    return f"The weather in {city} is 73 degrees and Sunny."

async def main():
    # Define an assistant agent
    weather_agent = AssistantAgent(
        name="weather_agent",
        model_client=OpenAIChatCompletionClient(
            model="gpt-4",  # Replace with the model version you intend to use
            api_key=api_key,
        ),
        tools=[get_weather],
    )

    # Define a team with a single agent and maximum auto-gen turns of 1
    agent_team = RoundRobinGroupChat([weather_agent], max_turns=1)

    while True:
        # Get user input from the console
        user_input = input("Enter a message (type 'exit' to leave): ")
        if user_input.strip().lower() == "exit":
            break
        # Run the team and stream messages to the console
        stream = agent_team.run_stream(task=user_input)
        await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())
