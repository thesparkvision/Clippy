from openai import OpenAI

from src.config.env import OPENAI_API_KEY

def get_openai_client():
    """
    Function to configure and return an instance of the OpenAI API client.
    """

    return OpenAI(api_key=OPENAI_API_KEY)
