
from api.constants import OpenAIModels
from api.utils.openai import get_openai_client

def get_prompt_result(prompt: str):
    openai_client = get_openai_client()
    response = openai_client.chat.completions.create(
        model=OpenAIModels.GPT_3_5_TURBO,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        n=1
    )

    if response:
        return response.choices[0].message.content
    