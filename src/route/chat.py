from http import HTTPStatus
from flask import Blueprint, request 
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.services import chat as chat_service

chat_ns = Namespace(name='chat', description='chat APIs', path='')

prompt_schema = chat_ns.model(name="prompt", model = {
    "prompt": fields.String(required=True)
})

@chat_ns.route("/openai-completion", methods=["POST"])
class OpenAICompletion(Resource):
    
    @chat_ns.doc(
        "Auth registration",
        responses={
            201: ("Successful Prompt Execution", prompt_schema),
            400: "Malformed data or validations failed.",
        }
    )
    @chat_ns.expect(prompt_schema, validate=True)
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()

        request_body = request.get_json()
        prompt = request_body['prompt']

        result = chat_service.get_prompt_result(user_id, prompt)
        return result