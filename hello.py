# from http://flask.pocoo.org/ tutorial
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/replace")
def hello():
    return render_template('replace.html')


@app.route("/build")
def hello():
    return render_template('build.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
