from flask_jwt_extended import create_access_token, create_refresh_token
import bcrypt

from src.models import User, UserToken
from src.utils.db import db

def register_user(full_name, email, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(full_name=full_name, email=email, password=hashed_password, is_active=True)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}
    return None

def create_token(user_id, expiry_date):
    new_token = UserToken(token="random_token", expiry_date=expiry_date, is_valid=True, user_id=user_id)
    db.session.add(new_token)
    db.session.commit()
    return new_token

def validate_token(token):
    user_token = UserToken.query.filter_by(token=token, is_valid=True).first()
    if user_token and user_token.expiry_date > datetime.utcnow():
        return True
    return False