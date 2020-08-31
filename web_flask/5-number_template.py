#!/usr/bin/python3
from web_flask import app
from flask import render_template


@app.route('/number_template/<n>', strict_slashes=False)
def template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
