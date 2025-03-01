#!/usr/bin/python3
"""a minimal app in Flask"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """A basic string returned in Flask"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns hbnb"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
