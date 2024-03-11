from flask import request
from flask_restx import Namespace, Resource, fields

from src.services import auth as auth_service
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_ns = Namespace('auth', path='', description='Authentication operations')

user_model = auth_ns.model('User', {
    'full_name': fields.String(required=True, description='User full name'),
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

login_model = auth_ns.model('Login', {
    'email': fields.String(required=True, description='User email address'),
    'password': fields.String(required=True, description='User password')
})

token_model = auth_ns.model('Token', {
    'access_token': fields.String(description='Access token'),
    'refresh_token': fields.String(description='Refresh token')
})


@auth_ns.route('/register')
class RegisterUser(Resource):
    @auth_ns.expect(user_model)
    @auth_ns.doc(responses={201: 'User registered successfully'})
    def post(self):
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        password = data.get('password')
        new_user = auth_service.register_user(full_name, email, password)
        return {'message': 'User registered successfully'}, 201

@auth_ns.route('/login')
class LoginUser(Resource):
    @auth_ns.expect(login_model)
    @auth_ns.doc(responses={200: 'Login successful', 401: 'Invalid credentials'})
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')
        tokens = auth_service.login_user(email, password)
        if tokens:
            return tokens, 200
        return {'message': 'Invalid credentials'}, 401