from flask import Blueprint, jsonify
from src.services.hello_world_service import HelloWorldService

hello_world_bp = Blueprint("hello_world", __name__)

hello_world_service = HelloWorldService()


@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    result = hello_world_service.execute()
    return jsonify(result)
