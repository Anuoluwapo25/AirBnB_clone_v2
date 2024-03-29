#!/usr/bin/python3
"""
script that starts a Flask web application
web application listening on 0.0.0.0 and port 5000
used strict_slashes=False in route definition
Routes  /: display “Hello HBNB!”
        /hbnb: display "HBNB"
        /c/<text>: displays custom text, replaces '_' with ' '
        /python/<text>: display custom text - default text = "is cool"
        /number/<n>: display “n is a number” only if n is an integer
"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    display "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """
    displays custom text, replaces '_' with ' '
    """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python")
@app.route("/python/<text>")
def python_route(text='is cool'):
    """
    displays custom text
    display default text is no argument is given as URL
    unique URL/Redirection behaviour
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>")
def number(n):
    """
    display text if ONLY n is a number
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
