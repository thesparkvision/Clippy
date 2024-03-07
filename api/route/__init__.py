from flask import Blueprint
from flask_restx import Api

from .chat import chat_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint)

api.add_namespace(chat_ns)