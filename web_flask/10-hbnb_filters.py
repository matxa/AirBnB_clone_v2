#!/usr/bin/python3
"""getting and rendering data from storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os
from flask import g


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """render html list"""
    s = storage.all(State)
    c = storage.all(City)
    a = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=s,
                           cities=c,
                           amenities=a)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
