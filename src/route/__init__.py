from flask import Blueprint
from flask_restx import Api

from .chat import chat_ns
from .auth import auth_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Enter your JWT token in the format "Bearer <token>"',
    }
}

api = Api(blueprint, authorizations = authorizations, security='apikey')

api.add_namespace(chat_ns)
api.add_namespace(auth_ns)