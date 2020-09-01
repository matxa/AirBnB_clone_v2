#!/usr/bin/python3
from web_flask import app
from flask import render_template


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
