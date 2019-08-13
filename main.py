import requests
import json
from pprint import pprint
import PlayerParser

def update_player_map():
    players = requests.get("https://api.sleeper.app/v1/players/nfl")
    with open('playerMap.json', 'w+') as playerMapFile:
        json.dump(players.json(), playerMapFile)
    return

leagueID = "386975772876750848"

firstTimeToday = False

if firstTimeToday:
    update_player_map()

pp = PlayerParser.PlayerParser(leagueID)
print pp.calculate_league_avg_ages()


# pp.print_scoring_settings()

pp.get_weekly_projections(1)