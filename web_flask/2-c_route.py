#!/usr/bin/python3
"""c/<routeVariable> route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def get_text(text):
    """get var from route"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
