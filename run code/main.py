import asyncio
from agent_config import agent_team, stopping_condition

async def main():
    """
    Asynchronous entry point for running the agent team in a conversational loop.
    """
    initial_message = (
        "Agent_1: Please generate Python code to calculate the factorial of a number. "
        "Agent_2: After Agent_1 generates the code, run it and provide the results. If there are any errors, report them and suggest fixes."
    )

    # Start the conversation stream with the initial message
    stream = agent_team.run_stream(task=initial_message)

    # Process messages as they arrive
    async for message in stream:
        if hasattr(message, "content"):
            print(f"{message.source}: {message.content}")

        # Stop the conversation if the stopping condition is triggered
        if stopping_condition(message):
            print("Stopping condition met. Ending conversation.")
            break

if __name__ == "__main__":
    asyncio.run(main())
