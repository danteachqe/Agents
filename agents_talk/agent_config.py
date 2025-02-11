import os
from autogen import ConversableAgent
from api_config import llm_config

# Define Agent_1 with its original role.
Agent_1 = ConversableAgent(
    name="Agent_1",
    system_message=(
        "Agent_1: You are a great python developer"
    ),
    llm_config=llm_config,
    code_execution_config=False,  # No code execution.
    function_map=None,
    human_input_mode="NEVER"
)

# Define Agent_2 with its original role, now including a termination condition.
Agent_2 = ConversableAgent(
    name="Agent_2",
    system_message=(
        "Agent_2: After Agent_1 proposes a solution, critique it and suggest any possible improvements or alternative methods. "
        "Continue discussing back and forth until you jointly conclude you've reached a robust solution. Also make sure the solution follows best industry practices and testing approaches."
        "when you are happy with the solution add the phrase 'final solution' to the response "
    ),
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
    # Terminate conversation as soon as a message contains "final solution"
    is_termination_msg=lambda msg: "final solution" in msg["content"].lower()
)
