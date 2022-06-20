from flask import Blueprint, Response, jsonify, request


api1 = Blueprint("api1", __name__, template_folder="templates")

@api1.route("/hello", methods=["GET"])
def sub_api1() -> Response :
    name = "Jane"
    args = request.args
    if "name" in args:
        name = args["name"]

    return jsonify({"type": "api1", "ret": f"Hello, {name}"})
