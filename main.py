import json
from pprint import pprint
import PlayerParser
import PlayerSorter
from update import *

firstTimeToday = False

league_IDs = open("league_ids", "r").read().split('\n')

print league_IDs

if firstTimeToday:
    update_player_map()
    update_player_stats_map()

for i in league_IDs:
    print "\n {} \n".format(i)
    pp = PlayerParser.PlayerParser(i)
    pp.calculate_league_starting_CMCs()

