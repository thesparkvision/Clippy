from flask import Flask

from src.route import blueprint
from src.config.env import DATABASE_URI
from src.config.db import db, migrate
from src.config.auth import jwt

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a random, secret key
    
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(blueprint, url_prefix='/api/')
    
    return app

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(debug=True, port=port)