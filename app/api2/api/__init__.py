
from flask import Blueprint
from .api2_1 import api2_1_bp
from .api2_2 import api2_2_bp


api2 = Blueprint("api2", __name__)
print(f"app api2 {__name__}")

api2.register_blueprint(api2_1_bp)
api2.register_blueprint(api2_2_bp)