#!/usr/bin/python3
"""using var in parenthis
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def get_text_py(text):
    """get text from var"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
