import requests
from datetime import date, datetime, timedelta


def send_request_json(url):
    """
    Sends a GET request to the specified URL and returns the response as JSON.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        dict: The JSON response from the server as a dictionary.

    Raises:
        Exception: If there is an error during the request or JSON conversion.
    """
    try:
        response = requests.get(url, verify=False)
        r_json = response.json()
        print(f"Response status : {response.status_code}\n")
        return r_json
    except Exception as e:
        print(f"Error :\n{e}")


def search_match_infos(key, value, match_infos):
    """
    Look for the specified key in the match_infos and update the match_infos

    Args:
        key (str): The key to look for in the match_infos.
        value (any): The value to update in the match_infos.
        match_infos (dict): The dictionary to update.

    Returns:
        dict: The updated match_infos.
    """
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
        match_infos["date"] = value[0:10]
        match_infos["hour"] = value[11:-4]
    elif key == "format":
        match_infos["format"] = f"{value['type']} of {value['length']}"
    elif key == "stage":
        match_infos["stage_name"] = value["name"]

    return match_infos


def search_event_infos(key, value, event_infos):
    """
    Look for the specified key in the event_infos and update the event_infos

    Args:
        key (str): The key to look for in the event_infos.
        value (any): The value to update in the event_infos.
        event_infos (dict): The dictionary to update.

    Returns:
        dict: The updated event_infos.
    """
    if key == "name":
        event_infos["name"] = value
    elif key == "region":
        event_infos["region"] = value
    elif key == "startDate":
        event_infos["startDate"] = value[0:10]
    elif key == "endDate":
        event_infos["endDate"] = value[0:10]
    elif key == "prize":
        event_infos["prize"] = f'{value["amount"]} {value["currency"]}'

    return event_infos


def show_infos(infos, type="Match"):
    """
    Print the infos of a match or an event

    Args:
        infos (dict): The infos to print.
        type (str, optional): The type of infos ("Match" or "Event"). Defaults to "Match".
    """
    print(f"\n{type} infos :")
    for key, value in infos.items():
        print(f"\t{key} : {value}")


def get_events(region="", event_name="", after=""):
    """
    Fetches events from the Octane.gg API based on the provided filters.

    Args:
        region (str, optional): The region to filter events by. Defaults to "".
        event_name (str, optional): The name to filter events by. Defaults to "".
        after (str, optional): The date to filter events by. Only events after this date will be returned. Defaults to "".

    Returns:
        list: A list of dictionaries, each representing an event and its details.

    Raises:
        Exception: If there is an error during the request or JSON conversion.
    """
    try:
        all_events = []
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
            event_infos = {
                "name": "TBD",
                "region": "TBD",
                "startDate": "TBD",
                "endDate": "TBD",
                "prize": "TBD",
            }
            for key, value in event.items():
                event_infos = search_event_infos(key, value, event_infos)
            all_events.append(event_infos)

            show_infos(type="Event", infos=event_infos)

        return all_events
    except Exception as e:
        print(f"Error :\n{e}")


def get_team_id(team_name):
    try:
        if team_name == "" or team_name == None:
            return ""
        r_json = send_request_json(f"https://zsr.octane.gg/teams?name={team_name}")
        print(f"Team {team_name} id : {r_json['teams'][0]['_id']}")

        return r_json["teams"][0]["_id"]
    except Exception as e:
        print(f"Error :\n{e}")


def get_event_id(event_name):
    try:
        if event_name == "" or event_name == None:
            return ""
        r_json = send_request_json(f"https://zsr.octane.gg/events?name={event_name}")
        print(f"Event {event_name} id : {r_json['events'][0]['_id']}")

        return r_json["events"][0]["_id"]
    except Exception as e:
        print(f"Error :\n{e}")


def get_matches(team="", region="", event="", after=""):
    """
    Fetches matches from the Octane.gg API based on the provided filters.

    Args:
        region (str, optional): The region to filter matches by. Defaults to "".
        team (str, optional): The team to filter matches by. Defaults to "".
        event_name (str, optional): The name to filter matches by. Defaults to "".
        after (str, optional): The date to filter matches by. Only matches after this date will be returned. Defaults to "".

    Returns:
        list: A list of dictionaries, each representing an match and its details.

    Raises:
        Exception: If there is an error during the request or JSON conversion.
    """
    try:
        all_matches = []
        team_id = get_team_id(team)
        event_id = get_event_id(event)

        url = "https://zsr.octane.gg/matches?"
        if team_id != "":
            url += f"team={team_id}&"
        if region != "":
            url += f"region={region}&"
        if event_id != "":
            url += f"event={event_id}&"
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
                "hour": "TBD",
                "format": "TBD",
                "blue_score": "0",
                "orange_score": "0",
            }
            for key, value in match.items():
                match_infos = search_match_infos(key, value, match_infos)

            all_matches.append(match_infos)

            show_infos(type="match", infos=match_infos)

        return all_matches
    except Exception as e:
        print(f"Error :\n{e}")


def send_notification(match, delay=30):
    """
    Send a notification when the match is about to start

    Args:
        match (dict): The match to notify.
        delay (int, optional): The delay in minutes before the match starts. Defaults to 30.
    """
    now = datetime.now()
    notification_sent = False

    match_date_str = match["date"]
    match_date = datetime.strptime(match_date_str, "%Y-%m-%dT%H:%M:%SZ")

    time_diff = match_date - now
    print(f"Match starting in : {str(time_diff)[:-7]} minutes")

    if time_diff < timedelta(minutes=0):
        print("Match is already over !")
    elif time_diff <= timedelta(minutes=delay) and not notification_sent:
        print("Match is about to start !")
        notification_sent = True
    else:
        print("Match is not about to start !")


def main():
    today = date.today()
    print(f"Today's date : {today}\n")

    team_input = input("Enter a team name : ")
    event_input = input("Enter an event name : ")
    region_input = input("Enter a region : ")
    after_input = input("Enter a date (YYYY-MM-DD) : ")

    # get_matches(
    #     region=region_input, team=team_input, event=event_input, after=after_input
    # )

    # get_events(region=region_input, event_name=event_input, after=after_input)


if __name__ == "__main__":
    main()
