#!/usr/bin/python3
"""HBNB route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
