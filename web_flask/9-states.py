#!/usr/bin/python3
"""a minimal app in Flask"""
from models import storage
from models.city import City
from models.state import State
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """A basic string returned in Flask"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def var_hbnb(text):
    """display “C ” followed by the value of the text variable"""
    if "_" in text:
        text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", defaults={'text': None})
@app.route("/python/<text>")
def def_hbnb(text):
    """display “Python ”, followed by the value of the text variable"""
    if not text:
        return "Python is cool"
    elif "_" in text:
        text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def is_it_number(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route("/states_list")
def states_list():
    """lists US states"""
    # query storage for states
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """cities_by_states, cities in a state"""
    # query all states in storage
    state0e3 = storage.all(State)
    return render_template('8-cities_by_states.html', states=state0e3)


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    """Display a state with a state_id option"""
    state0e3 = storage.all(State)
    if state0e3 and id:
        key = f"State.{id}"
        return render_template('9-states.html', key=key, states=state0e3)
    # if no id, redirect to url_for /states_list
    return render_template('7-states_list.html', states=state0e3)


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """closes storage conns after a request context"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
