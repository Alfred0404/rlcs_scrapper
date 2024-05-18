# RLCS SCRAPPER

## Description

This little project is a web app that shows some informations about Rocket League esport matches or tournaments.
Users can browse matches or events from the API with different filters, and choose the matches for which they want to be notified.

As

## Installation

1. Install the libraries :
   - [requests](https://pypi.org/project/requests/)    `pip install requests`
   - [datatime](https://docs.python.org/3/library/datetime.html)   `pip install datetime`
   - [flask](https://flask.palletsprojects.com/en/3.0.x/)    `pip install flask`

## Usage

Currently, you chan choose to run only the `main.py` file, or the entire flask app, by running `python -m flask run` in your terminal, then click the localhost link.
Once on the web app, you can navigate to the matches page or the events page, to start gather informations about everything you want.

![matches page](image/README/rl_esport_home_page.png "home page")

On the matches page, you can filter matches by :

- Region
- Team
- Event
- Date

For every match on this page, you can choose to be notified to it, just by clicking the "Get notified" button.
![matches page](image/README/rl_esport_matches_page.png "matches page")

Same for the events page, you can filter events by :

- Region
- Event Name
- Date

For every event on the page, you can click the "See matches" button. It will redirect you on the "matches" page, where you will find all the matches of this event.
![matches page](image/README/rl_esport_events_page.png "events page")

## API

I'm using the [octane.gg](https://zsr.octane.gg/)'s API. It's an API that let you browse loads of interesting infos about everything that can happen in Rocket League esport (matches, events, teams, players, records, and a bunch of other stats).

## Contributing

PR are welcomed, contribute as much as you want, I'll be happy to discuss about features or fixes that you could bring to the project.
Don't hesitate as well to submit some issues if you encounter some, so we can fix it quickly.

- ⭐ Star this repository
- 🍴 Fork this repo
- 💻 Clone your forked repo
- ➕ Make your changes
- ✅ Commit, push
- ⌨️ Create a pull request
