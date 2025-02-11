from agent_config import Agent_1, Agent_2

def main():
    # Initiate the chat with a dynamic prompt.
    result = Agent_2.initiate_chat(
        Agent_1,
        message=(
            "Agent_1, please propose a python function that will calculate the factorial of a number "
            
                    ),
        max_turns=10  # Adjust maximum turns as needed.
    )
    
    print("Conversation result:")
    print(result)

if __name__ == "__main__":
    main()
