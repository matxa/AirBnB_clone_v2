#!/usr/bin/python3
"""getting and rendering data from storage
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
import os
from flask import g


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def filters():
    """render html list"""
    s = storage.all(State)
    c = storage.all(City)
    a = storage.all(Amenity)
    p = storage.all(Place)
    u = storage.all(User)
    return render_template('100-hbnb.html',
                           states=s,
                           cities=c,
                           amenities=a,
                           users=u,
                           places=p)


@app.teardown_appcontext
def teardown_db(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
