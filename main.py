import requests
import json
from pprint import pprint
import PlayerParser


leagueID = str(386975772876750848)

firstTimeToday = False

if firstTimeToday:
    players = requests.get("https://api.sleeper.app/v1/players/nfl")
    pprint(players.json())
    with open('playerMap.json', 'w+') as playerMapFile:
        json.dump(players.json(), playerMapFile)




pp = PlayerParser.PlayerParser()


pp.get_team_average_age(0)



print pp.calculate_league_avg_ages()



# pprint(t)