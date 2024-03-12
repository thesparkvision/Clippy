from src.constants import OpenAIModels
from src.config.openai import get_openai_client
from src.database import get_user_prompts, save_prompt_result

def get_prompt_result(user_id: int, prompt: str):

    openai_client = get_openai_client()

    chat_messages = [{"role": "system", "content": "You are a helpful assistant."}]

    prompt_results = get_user_prompts(user_id)
    
    for prompt_result in prompt_results:
        if prompt_result.prompt:
            chat_messages.append({"role": "user", "content": prompt_result.prompt})
        if prompt_result.result:
            chat_messages.append({"role": "assistant", "content": prompt_result.result})

    chat_messages.append({"role": "user", "content": prompt})

    response = openai_client.chat.completions.create(
        model=OpenAIModels.GPT_3_5_TURBO,
        messages=chat_messages,
        n=1
    )

    prompt_result = None
    if response:
        prompt_result = response.choices[0].message.content

    save_prompt_result(prompt, prompt_result, user_id)

    return prompt_result