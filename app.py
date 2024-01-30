from flask import Flask, render_template
from main import get_matches, get_events

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/matches")
def matches():
    return render_template("matches.html", matches=get_matches())


@app.route("/events")
def events():
    return render_template("events.html", events=get_events())
