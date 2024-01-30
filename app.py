from flask import Flask, render_template, request
from main import get_matches, get_events

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/matches", methods=["GET", "POST"])
def matches():
    if request.method == "POST":
        team = request.form.get("team")
        region = request.form.get("region")
        event = request.form.get("event")
        after = request.form.get("after")
        print(f"team : {team}\nregion : {region}\nevent : {event}\nafter : {after}")
        return render_template(
            "matches.html", matches=get_matches(team, region, event, after)
        )
    else:
        return render_template("matches.html", matches=get_matches())


@app.route("/events", methods=["GET", "POST"])
def events():
    if request.method == "POST":
        region = request.form.get("region")
        event_name = request.form.get("event_name")
        after = request.form.get("after")
        return render_template(
            "events.html", events=get_events(region, event_name, after)
        )
    else:
        return render_template("events.html", events=get_events())
