import os
from autogen import ConversableAgent
from api_config import llm_config

# Define Agent_1 with its original role.
Agent_1 = ConversableAgent(
    name="Agent_1",
    system_message=(
        "Agent_1: Please propose a list of test cases that will cover the use cases in the story. Follow best practices fro test case definition."
    ),
    llm_config=llm_config,
    code_execution_config=False,  # No code execution.
    function_map=None,
    human_input_mode="NEVER"
)

# Define Agent_2 with its original role and add a termination condition.
Agent_2 = ConversableAgent(
    name="Agent_2",
    system_message=(
        "Agent_2: After Agent_1 proposes software test cases, critique it and suggest any possible improvements "
        "Continue discussing back and forth until you jointly conclude you've reached a test case defintion "
        "Also make sure the solution follows best industry practices and testing approaches."
        "when you are happy with the final result simply say goodbye to end the conversion"
    ),
    llm_config=llm_config,
    code_execution_config=False,
    function_map=None,
    human_input_mode="NEVER",
    # Terminate the conversation if any reply contains "final solution:" (case-insensitive).
    is_termination_msg=lambda msg: "goodbye" in msg["content"].lower()
)
