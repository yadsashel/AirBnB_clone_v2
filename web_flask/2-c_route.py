#!/usr/bin/python3

""" script that starts a Flask web application with the following requirements:

The application must be listening on 0.0.0.0, port 5000.
The route / must display "Hello HBNB!".
The route /hbnb must display "HBNB".
The route /c/<text> must display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space). """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
