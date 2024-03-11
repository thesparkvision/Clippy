from http import HTTPStatus
from flask import Blueprint, request 
from flask_restx import Resource, Namespace, fields

from api.services import chat as chat_service

chat_ns = Namespace(name='chat', description='chat APIs', path='/')

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
        },
    )
    @chat_ns.expect(prompt_schema, validate=True)
    def post(self):
        request_body = request.get_json()
        prompt = request_body['prompt']

        result = chat_service.get_prompt_result(prompt)
        return result