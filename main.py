import requests
from datetime import date


def search_match_infos(key, value, match_infos, team_name=None):
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


def show_match_infos(match_infos):
    print("\nNew match :")
    for key, value in match_infos.items():
        print(f"\t{key} : {value}")


def get_upcoming_events(date):
    try:
        response = requests.get(
            f"https://zsr.octane.gg/events?after={date}", verify=False
        )
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        print(f"Upcoming events after {date} :")

        for event in r_json["events"]:
            print("New event :")
            print(f"\tName : {event['name']}")
            print(f"\tStart date : {event['startDate']}")
            print(f"\tEnd date : {event['endDate']}")
            print(f"\tRegion : {event['region']}")
            print()

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def get_upcoming_matches(date):
    try:
        response = requests.get(
            f"https://zsr.octane.gg/matches?after={date}", verify=False
        )
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        print(f"Upcoming matches after {date} :")

        for match in r_json["matches"]:
            match_infos = {
                "event_name": "TBD",
                "event_region": "TBD",
                "stage_name": "TBD",
                "blue_team": "TBD",
                "orange_team": "TBD",
                "date": "TBD",
                "format": "TBD",
                "blue_score": "TBD",
                "orange_score": "TBD",
            }
            for key, value in match.items():
                match_infos = search_match_infos(key, value, match_infos)

            show_match_infos(match_infos)

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def get_team_all_matches(team_name, date):
    try:
        print(f"Matches of {team_name} after {date} :")
        matches_json = requests.get(
            f"https://zsr.octane.gg/matches?after={date}", verify=False
        ).json()

        for match in matches_json["matches"]:
            match_infos = {
                "event_name": "TBD",
                "event_region": "TBD",
                "stage_name": "TBD",
                "blue_team": "TBD",
                "orange_team": "TBD",
                "date": "TBD",
                "format": "TBD",
                "blue_score": "TBD",
                "orange_score": "TBD",
            }

            for key, value in match.items():
                match_infos = search_match_infos(key, value, match_infos)

            if (
                match_infos["blue_team"] == team_name
                or match_infos["orange_team"] == team_name
            ):
                show_match_infos(match_infos)
    except Exception as e:
        print(f"Error :\n{e}")


def main():
    today = date.today()
    print(f"Today's date : {today}\n")

    # get_upcoming_events(today)
    # get_upcoming_matches(today)
    get_team_all_matches("Gros Noobz", today)


if __name__ == "__main__":
    main()
