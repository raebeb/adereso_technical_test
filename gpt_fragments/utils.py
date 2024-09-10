import json
from urllib.parse import urlparse
from gpt_fragments.api_client import GPTClient

def read_jsonl(file_path: str):
    """
    Read a JSONL file and yield each JSON object.

    Args:
        file_path (str): The path to the JSONL file.

    Yields:
        dict: A JSON object parsed from each line in the file.
    """    
    with open(file_path, 'r') as file:
        for line in file:
            yield json.loads(line)

def write_jsonl(file_path: str, data: list):
    """
    Write a list of dictionaries to a JSON Lines file.

    Args:
        file_path (str): The file path where the JSON Lines file will be written.
        data (list): A list of dictionaries to be written to the file.

    Returns:
        None
    """    
    with open(file_path, 'w') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')


def get_prompt_based_on_context(context: str, gpt_client: GPTClient) -> str:
    """
    Get a prompt based on a specific context using GPT API.

    Args:
        context (str): The context for which to retrieve a prompt.
        gpt_client (GPTClient): An instance of the GPTClient class.

    Returns:
        str: The generated prompt corresponding to the input context.
    """
    if context is None:
        context = "general"

    return gpt_client.generate_prompt(context)


def get_article_context(url: str, gpt_client: GPTClient) -> str:
    """
    Get the context of an article based on its URL.

    Args:
        url (str): The URL of the article.
        gpt_client (GPTClient): An instance of the GPTClient class.

    Returns:
        str: The context of the article based on the URL.
    """    
    parsed_url = urlparse(url)
    path = parsed_url.path
    context = path.lstrip("/").split("/")[0]
    return get_prompt_based_on_context(context, gpt_client)
