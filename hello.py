""" print a hello world"""

from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def hello():
    """   helllo"""
    return "Hello World!"


if __name__ == "__main__":
    APP.run(host="0.0.0.0")
