from enum import Enum
from datetime import datetime
from sqlalchemy import Enum as EnumSQL

from src.utils.db import db

class TokenType(Enum):
    ACCESS = 'access'
    REFRESH = 'refresh'

class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id
    
    def __str__(self):
        return '<User %r>' % self.id

class UserToken(BaseModel):
    __tablename__ = 'user_tokens'

    id = db.Column(db.Integer, primary_key=True)
    token_type = db.Column(EnumSQL(TokenType), nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    is_valid = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    user = db.relationship('User', backref='user_tokens')

    def __repr__(self):
        return f"<Token {self.id}>"

    def __str__(self):
        return f"<Token {self.id}>"