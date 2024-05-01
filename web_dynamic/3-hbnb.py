#!/usr/bin/python3
"""this script starts a Flask web application
    this web application must be listening on 0.0.0.0 at port 5000
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
from uuid import uuid4

app = Flask(__name__)


@app.route("/3-hbnb/", strict_slashes=False)
def hbnb_filters():
    """Displays an HTML page with a hbnb_filters
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("3-hbnb.html", states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=str(uuid4()))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001")
