#!/usr/bin/python3

"""run flask server"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """hello returned"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=True)
def hbnb():
    """hbnb returned"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
