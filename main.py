import requests
from datetime import date


def send_request_json(url):
    try:
        response = requests.get(url, verify=False)
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def search_match_infos(key, value, match_infos):
    if key == "event":
        match_infos["event_name"] = value["name"]
        match_infos["event_region"] = value["region"]
    if key == "blue":
        match_infos["blue_team"] = value["team"]["team"]["name"]
        try:
            match_infos["blue_score"] = value["score"]
        except KeyError:
            pass
    elif key == "orange":
        match_infos["orange_team"] = value["team"]["team"]["name"]
        try:
            match_infos["orange_score"] = value["score"]
        except KeyError:
            pass
    elif key == "date":
        match_infos["date"] = value
    elif key == "format":
        match_infos["format"] = f"{value['type']} of {value['length']}"
    elif key == "stage":
        match_infos["stage_name"] = value["name"]

    return match_infos


def show_infos(infos, type="Match"):
    print(f"\n{type} infos :")
    for key, value in infos.items():
        print(f"\t{key} : {value}")


def get_events(region="", event_name="", after=""):
    try:
        url = "https://zsr.octane.gg/events?"
        if region != "":
            url += f"region={region}&"
        if event_name != "":
            url += f"name={event_name}&"
        if after != "":
            url += f"after={after}&"

        r_json = send_request_json(url)
        print(f"Upcoming events after {date} :")

        for event in r_json["events"]:
            show_infos(type="event", infos=event)

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def get_team_id(team_name):
    try:
        if team_name == "":
            return ""
        r_json = send_request_json(f"https://zsr.octane.gg/teams?name={team_name}")
        print(f"Team {team_name} id : {r_json['teams'][0]['_id']}")

        return r_json["teams"][0]["_id"]
    except Exception as e:
        print(f"Error :\n{e}")


def get_matches(team="", region="", event="", after=""):
    try:
        team_id = get_team_id(team)

        url = "https://zsr.octane.gg/matches?"
        if team_id != "":
            url += f"team={team_id}&"
        if region != "":
            url += f"region={region}&"
        if event != "":
            url += f"event={event}&"
        if after != "":
            url += f"after={after}&"

        r_json = send_request_json(url)

        for match in r_json["matches"]:
            match_infos = {
                "event_name": "TBD",
                "event_region": "TBD",
                "stage_name": "TBD",
                "blue_team": "TBD",
                "orange_team": "TBD",
                "date": "TBD",
                "format": "TBD",
                "blue_score": "0",
                "orange_score": "0",
            }
            for key, value in match.items():
                match_infos = search_match_infos(key, value, match_infos)

            show_infos(type="match", infos=match_infos)

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def main():
    today = date.today()
    print(f"Today's date : {today}\n")
    team_input = input("Enter a team name : ")
    event_input = input("Enter an event name : ")
    region_input = input("Enter a region : ")
    after_input = input("Enter a date (YYYY-MM-DD) : ")

    get_matches(
        region=region_input, team=team_input, event=event_input, after=after_input
    )


if __name__ == "__main__":
    main()
