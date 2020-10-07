#!/usr/bin/python3
"""Helo route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello route"""
    return "Hello HBNB!"

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():   
    """deploying first version
    of airbnb project
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
