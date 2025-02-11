import os

def get_openai_api_key() -> str:
    """
    Retrieve the OpenAI API key from environment variables.
    
    Raises:
        ValueError: If the OPENAI_API_KEY environment variable is not set.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    return api_key

# Configuration for the language model. 
llm_config = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": get_openai_api_key(),
        }
    ]
}
