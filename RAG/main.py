from agent_config import Agent_1, Agent_2
from document_processor import RAGProcessor

def main():
    # Specify the path to your external document.
    file_path = r"C:\Users\Dan\Desktop\mails\story.txt"  

    # Create a RAGProcessor instance to load and process the document.
    processor = RAGProcessor(file_path)

    # Define your query or task.
    query = (
        "Agent_1, please propose a list of test cases based on the content of the user story "
        "Follow industry best practices."
    )
    
    # Process the query by combining it with the document content.
    prompt = processor.process_query(query)
    
    # Initiate the conversation using Agent_2 (with its termination condition) with Agent_1.
    result = Agent_2.initiate_chat(
        Agent_1,
        message=prompt,
        max_turns=10  # Adjust the maximum number of turns as needed.
    )
    
    print("Conversation result:")
    print(result)

if __name__ == "__main__":
    main()
