#!/usr/bin/python3
"""
 a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Display 'c'.
    /python/<text>: Display 'python'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_what(text):
    """Displays 'C' followed by  <text>."""
    t = text.replace("_", " ")
    return "C {}".format(t)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_what(text = 'is cool'):
    """Displays 'C' followed by  <text>."""
    t = text.replace("_", " ")
    return "Python {}".format(t)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
