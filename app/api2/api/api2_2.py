

from flask import Blueprint, Response, jsonify, request

api2_2_bp = Blueprint("api2_2", __name__)

@api2_2_bp.route("/hello3", methods=["GET"])
def sub_api2() -> Response :
    name = "No-Name"
    args = request.args
    if "name" in args:
        name = args["name"]

    return jsonify({"type":"api2", "ret": f"How are you, {name}?"})