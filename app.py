from flask import Flask, render_template, request
from main import get_matches, get_events, show_infos, send_notification
import json

app = Flask(__name__)


@app.route("/")
def index():
    """
    Handle the index page requests

    Returns:
        HTML: The HTML page with the index
    """
    return render_template("index.html")


@app.route("/matches", methods=["GET", "POST"])
def matches():
    """
    Handle the matches page requests

    Returns:
        HTML: The HTML page with the matches
    """
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


@app.route("/notify", methods=["POST"])
def notify():
    """
    Handle the notification requests

    Returns:
        str: Empty string so it doesn't reload the page
    """
    if request.method == "POST":
        match_info = request.form.get("match_info").replace("'", '"')
        match_info_json = json.loads(match_info)

        print("You will be notified before this match starts :")
        show_infos(type="Match", infos=match_info_json)
        send_notification(match_info_json)

        return "", 204


@app.route("/events", methods=["GET", "POST"])
def events():
    """
    Handle the events page requests

    Returns:
        HTML: The HTML page with the events
    """
    if request.method == "POST":
        region = request.form.get("region")
        event_name = request.form.get("event_name")
        after = request.form.get("after")

        return render_template(
            "events.html", events=get_events(region, event_name, after)
        )
    else:
        return render_template("events.html", events=get_events())
