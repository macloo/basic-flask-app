
from flask import Blueprint, Response, jsonify, request

api2_1_bp = Blueprint("api2_1", __name__)


@api2_1_bp.route("/hello", methods=["GET"])
@api2_1_bp.route("/helloagain", methods=["GET"])
def sub_api1() -> Response :
    name = "Jon"
    args = request.args
    if "name" in args:
        name = args["name"]

    return jsonify({"type":"api2", "ret": f"Hello again, {name}"})