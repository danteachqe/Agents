import os
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen.executors.local_commandline_code_executor import LocalCommandLineCodeExecutor

def get_openai_api_key() -> str:
    """
    Retrieve the OpenAI API key from environment variables.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    return api_key

def stopping_condition(message) -> bool:
    """
    Check if the stopping condition is met.
    
    For example, we stop if the message content contains 'execution complete'.
    """
    if hasattr(message, "content"):
        return "execution complete" in message.content.lower()
    return False

class CodeGeneratingAgent(AssistantAgent):
    """
    Custom assistant agent for generating Python code.
    """
    async def on_message(self, message):
        """
        Generate Python code based on the provided task.
        """
        if hasattr(message, "content"):
            prompt = f"Please generate Python code for the following task:\n\n{message.content}"
            response = await self.model_client.chat_completion(prompt)
            return response

class CodeExecutionAgent(AssistantAgent):
    """
    Custom assistant agent for executing Python code using LocalCommandLineCodeExecutor.
    """
    def __init__(self, name, model_client):
        super().__init__(name=name, model_client=model_client)
        self.executor = LocalCommandLineCodeExecutor()  # Use LocalCommandLineCodeExecutor

    async def on_message(self, message):
        """
        Execute the generated Python code using LocalCommandLineCodeExecutor.
        """
        if hasattr(message, "content"):
            python_code = message.content.strip()
            print(f"Executing Code:\n{python_code}")  # Debug: Display the code to be executed

            # Execute the code using LocalCommandLineCodeExecutor
            result = self.executor.execute(
                language="python",  # Specify the programming language
                code=python_code    # The Python code to execute
            )

            if result.error:
                return f"Execution Error:\n{result.error}"
            return f"Execution Output:\n{result.output}"

# Create Agent 1: Generates Python code
agent_1 = CodeGeneratingAgent(
    name="agent_1",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4",
        api_key=get_openai_api_key(),
    ),
)

# Create Agent 2: Executes Python code using LocalCommandLineCodeExecutor
agent_2 = CodeExecutionAgent(
    name="agent_2",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4",
        api_key=get_openai_api_key(),
    ),
)

# Configure the team to round-robin between both agents, up to 10 turns
agent_team = RoundRobinGroupChat(
    [agent_1, agent_2],
    max_turns=10
)
