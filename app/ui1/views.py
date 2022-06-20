#
from flask import request
from flask import Blueprint, render_template

ui1 = Blueprint('func1', __name__, template_folder='templates')
print(f"app func1 {__name__}", __name__)


@ui1.route("/", methods=['GET', 'POST'])
@ui1.route("/sub_func1", methods=['GET', 'POST'])
def sub_func1() -> str:
    name = ""
    if request.method == "POST":
        name=request.form.get("name","")
    else:
        name=request.args.get("name", "")
    return render_template("func1_temp.html", the_title="Blueprint view page home", name=name )
