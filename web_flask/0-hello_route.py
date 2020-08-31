#!/usr/bin/python3
from __init__ import app


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
