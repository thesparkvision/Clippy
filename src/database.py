from src.models import PromptResult
from src.config.db import db

def get_user_prompts(user_id: int):
    prompt_results = PromptResult.query.filter_by(user_id=user_id).order_by(PromptResult.created_at.asc()).all()
    return prompt_results

def save_prompt_result(prompt: str, result: str, user_id: int):
    new_result = PromptResult(prompt=prompt, result=result, user_id=user_id)
    db.session.add(new_result)
    db.session.commit()
    return new_result