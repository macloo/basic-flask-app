from flask import Flask, render_template

from app.ui1.views import ui1
from app.api1.api import api1
from app.api2.api import api2

app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@app.route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@app.route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')

if __name__ == '__main__':
    app.register_blueprint(ui1, url_prefix="/ui")
    app.register_blueprint(api1, url_prefix="/api1")
    app.register_blueprint(api2, url_prefix="/api2")
    app.run(debug=True)
