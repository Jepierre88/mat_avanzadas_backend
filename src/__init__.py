from flask import Flask
from src.controllers.hello_world_controller import hello_world_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints (controllers)
    app.register_blueprint(hello_world_bp)

    return app
