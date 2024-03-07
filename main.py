from flask import Flask
from api.route import blueprint

def create_app():
    app = Flask(__name__)

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