#!/usr/bin/python3
from web_flask import app


@app.route('/number/<n>', strict_slashes=False)
def get_text_py(n):
    # if type(n) is int:
    #     return "{} is a number".format(n)
    return "{}".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
