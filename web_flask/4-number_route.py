#!/usr/bin/python3
from web_flask import app


@app.route('/number/<int:n>', strict_slashes=False)
def get_int(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
