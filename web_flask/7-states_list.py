#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    remove the current session
    """
    storage.close()



app.route("/states_list", strict_slashes=False)
def states_lists():
    """
    dispaly HtMl PAGE
    """
    states = storage.all(State)
    sorted_state =  [states[key] for key in states]
    return(render_template("7-states_list.html", states=sorted_state))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
