import requests
from datetime import date


def get_upcoming_events(date):
    try:
        response = requests.get(f"https://zsr.octane.gg/events?after={date}", verify=False)
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
        response = requests.get(f"https://zsr.octane.gg/matches?after={date}", verify=False)
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        print(f"Upcoming matches after {date} :")

        for match in r_json["matches"]:
            stage_name = "TBD"
            orange = "TBD"
            blue = "TBD"
            orange_score = "0"
            blue_score = "0"
            event_name = "TBD"
            event_region = "TBD"
            date = "TBD"
            format = "TBD"

            print("New match :")
            for key, value in match.items():
                if key == "event":
                    event_name = value["name"]
                    event_region = value["region"]
                if key == "blue":
                    blue = value["team"]["team"]["name"]
                    try:
                        blue_score = value["score"]
                    except KeyError:
                        pass
                elif key == "orange":
                    orange = value["team"]["team"]["name"]
                    try:
                        orange_score = value["score"]
                    except KeyError:
                        pass
                elif key == "date":
                    date = value
                elif key == "format":
                    format = f"{value['type']} of {value['length']}"
                elif key == "stage":
                    stage_name = value["name"]

            print(f"\tEvent : {event_name}")
            print(f"\tRegion : {event_region}")
            print(f"\tStage : {stage_name}")
            print(f"\tBlue : {blue}")
            print(f"\tOrange : {orange}")
            print(f"\tDate : {date}")
            print(f"\tFormat : {format}")
            if blue_score and orange_score:
                print(f"\tScore : {blue} : {blue_score} - {orange_score} : {orange}")
            print()

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def get_match_games(match_id):
    try:
        response = requests.get(f"https://zsr.octane.gg/matches{match_id}/games", verify=False)
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        print(f"Games of match {match_id} :")

        for game in r_json["games"]:
            print("New game :")
            print(f"\tMatch : {game['match']['id']}")
            print(f"\tGame : {game['number']}")
            print(f"\tDate : {game['date']}")
            print(f"\tBlue : {game['blue']['team']['team']['name']}")
            print(f"\tOrange : {game['orange']['team']['team']['name']}")
            print(f"\tBlue score : {game['blue']['team']['stats']['core']['goals']}")
            print(f"\tOrange score : {game['orange']['team']['stats']['core']['goals']}")
            print()

        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def main():
    today = date.today()
    print(f"Today's date : {today}\n")

    get_upcoming_events(today)
    get_upcoming_matches(today)


if __name__ == "__main__":
    main()