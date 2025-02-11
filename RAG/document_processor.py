import os

def read_local_document(file_path: str) -> str:
    """
    Reads the content of a local text file and returns it as a string.
    
    Args:
        file_path (str): The path to the document.
        
    Returns:
        str: The content of the document.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the document content is empty.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found at {file_path}.")
    # Use utf-8 encoding as best practice when reading text files.
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    if not content.strip():
        raise ValueError(f"The document at {file_path} is empty or could not be read.")
    return content

class RAGProcessor:
    """
    Handles Retrieval-Augmented Generation for document-based tasks.
    
    This class loads a document from a given path and provides a method to combine
    that document's content with a query to produce a clear, structured prompt.
    """
    def __init__(self, document_path: str):
        self.document_path = document_path
        self.document_content = self.load_document()

    def load_document(self) -> str:
        """
        Loads the document content using read_local_document and ensures it is not empty.
        
        Returns:
            str: The content of the document.
            
        Raises:
            ValueError: If the document content is empty.
        """
        content = read_local_document(self.document_path)
        # Debug output: print the first 500 characters.
        print(f"Document Content Loaded (first 500 chars):\n{content[:500]}")
        return content

    def process_query(self, query: str) -> str:
        """
        Combines the query with the document content to create a clear, structured prompt.
        
        Args:
            query (str): The query or task to be augmented.
        
        Returns:
            str: A combined prompt that includes both the document context and the task.
        """
        full_prompt = (
            f"### Document Context ###\n"
            f"{self.document_content}\n\n"
            f"### Task ###\n"
            f"{query}"
        )
        # Debug output: print the first 500 characters of the generated prompt.
        print(f"Generated Prompt (first 500 chars):\n{full_prompt[:500]}")
        return full_prompt
