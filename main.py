import requests
import json
from pprint import pprint
import PlayerParser


r = requests.get("https://api.sleeper.app/v1/league/412718806528438272/rosters")
x = r.json()

firstTimeToday = False

if firstTimeToday:
    players = requests.get("https://api.sleeper.app/v1/players/nfl")
    pprint(players.json())
    with open('playerMap.json', 'w+') as playerMapFile:
        json.dump(players.json(), playerMapFile)


q = requests.get("https://api.sleeper.app/v1/stats/nfl/regular/2018/16")
qq = q.json()
pprint(qq)

pp = PlayerParser.PlayerParser()

for i in x[0]['starters']:
    print pp.get_player_name(i)



