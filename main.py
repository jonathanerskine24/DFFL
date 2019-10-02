import requests
import json
from pprint import pprint
import PlayerParser

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

leagueID = "386975772876750848"

firstTimeToday = False


if firstTimeToday:
    update_player_map()
    update_player_stats_map()


pp = PlayerParser.PlayerParser(leagueID)
print pp.calculate_league_avg_ages()


pp.calculate_league_player_ranks()