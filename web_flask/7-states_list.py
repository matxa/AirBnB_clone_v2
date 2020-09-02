#!/usr/bin/python3
"""getting and rendering data from storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os
from flask import g


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def render_state_obj():
    """render html list"""
    list_of_states = storage.all(State)
    return render_template('7-states_list.html', states=list_of_states)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
