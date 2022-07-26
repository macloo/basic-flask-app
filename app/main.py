from flask import Flask, render_template, render_template_string
from flask import request
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

@app.route('/hello')
def hello():
    return render_template_string("<div>Hello: %s</div>" % request.args.get("name"))

if __name__ == '__main__':
    app.run(debug=True)
