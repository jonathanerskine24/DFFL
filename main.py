import requests
import json
from pprint import pprint
import PlayerParser
import PlayerSorter

def update_player_map():
    players = requests.get("https://api.sleeper.app/v1/players/nfl")
    with open('playerMap.json', 'w+') as playerMapFile:
        json.dump(players.json(), playerMapFile)
    return

def update_player_stats_map():
    player_stats = requests.get("https://api.sleeper.app/v1/stats/nfl/regular/2019")
    with open('playerStatsMap.json', 'w+') as playerStatsMapFile:
        json.dump(player_stats.json(), playerStatsMapFile);
    return

FlorabamaID = "386975772876750848"
SpringsID = "475384173494792192"

firstTimeToday = False

if firstTimeToday:
    update_player_map()
    update_player_stats_map()

pp = PlayerParser.PlayerParser(FlorabamaID)
pp2 = PlayerParser.PlayerParser(SpringsID)

pp.print_lists()

print "\nFlorabama\n"
pp.calculate_league_starting_CMCs()
pp.calculate_league_pos_ranks()
print "\nSprings\n"
pp2.calculate_league_pos_ranks()