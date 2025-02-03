import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Define the first agent
agent_1 = AssistantAgent(
    name="agent_1",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4",
        api_key=os.getenv("OPENAI_API_KEY"),
    ),
)

# Define the second agent
agent_2 = AssistantAgent(
    name="agent_2",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4",
        api_key=os.getenv("OPENAI_API_KEY"),
    ),
)

# Set up a team with both agents
agent_team = RoundRobinGroupChat([agent_1, agent_2], max_turns=10)

# Define a stopping condition
def stopping_condition(message) -> bool:
    """
    Check if the stopping condition is met.
    For example, stop if the message content contains 'correct answer'.
    """
    if hasattr(message, "content"):
        return "correct answer" in message.content.lower()
    return False

async def main():
    # A more interactive initial message prompting the agents to discuss
    initial_message = (
    "Agent_1: Please propose a Python function to compute the square root of a number. "
    "Agent_2: After Agent_1 proposes a solution, critique it and suggest any possible "
    "improvements or alternative methods. Continue discussing back and forth until you "
    "jointly conclude you've reached a robust solution."
   )

    stream = agent_team.run_stream(task=initial_message)

    # Iterate through the messages
    async for message in stream:
        if hasattr(message, "content"):
            print(f"{message.source}: {message.content}")

        # Check if the stopping condition is met
        if stopping_condition(message):
            print("Stopping condition met. Ending conversation.")
            break

if __name__ == "__main__":
    asyncio.run(main())
