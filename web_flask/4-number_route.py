#!/usr/bin/python3
"""c/num
"""
from flask import Flask


app = Flask(__name__)


@app.route('/number/<int:n>', strict_slashes=False)
def get_int(n):
    """check if var is int"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
