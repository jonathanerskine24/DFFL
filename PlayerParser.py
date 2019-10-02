import json
import requests 
from pprint import pprint

class PlayerParser():

    def initialize_userID_map(self):
        t = requests.get("https://api.sleeper.app/v1/league/386975772876750848/users").json()
        self.userIDmap = {}
        for x in t:
            self.userIDmap[x['user_id']] = x['display_name']
        return

    def get_league_info(self, league_id):
        self.leagueInfo = requests.get("https://api.sleeper.app/v1/league/" + league_id).json()
        self.scoringSettings = self.leagueInfo["scoring_settings"]
        self.initialize_userID_map()
        return

    def get_roster_info(self, league_id):
        self.rosterInfo = requests.get("https://api.sleeper.app/v1/league/" + league_id + "/rosters").json()
        return


    def __init__(self, league_id):

        # get league info
        self.get_league_info(league_id)

        # get roster info
        self.get_roster_info(league_id)

        # load player data file
        with open("playerMap.json", 'r') as f:
             self.playerData = json.load(f)

        #load player stats file
        with open("playerStatsMap.json", "r") as f:
            self.playerStats = json.load(f)

        return
    
    # methods for getting player attributes

    def get_player_name(self, playerID):
        if self.playerData[playerID]['position'] != "DEF":
            return self.playerData[playerID]['full_name']
        else:
            return self.playerData[playerID]['last_name'] + " D/ST"

    def get_player_age(self, playerID):
        if self.playerData[playerID]['position'] != "DEF":
            return self.playerData[playerID]['age']
        else:
            return 0

    # methods for analyizing teams

    def get_username(self, user_id):
        return self.userIDmap[str(user_id)]

    def get_team_average_age(self, teamID):
        totalAge = 0
        nonDefensePlayers = 0
        playerIDs = self.rosterInfo[teamID]['players']
        for p in playerIDs:
            player_age = self.get_player_age(p)
            if player_age != -1:
                totalAge = totalAge + player_age
                nonDefensePlayers += 1

        return ( float(totalAge) / nonDefensePlayers)
    
    def get_team_player_ranks(self, teamID):
        playerIDs = self.rosterInfo[teamID]['players']
        for p in playerIDs:
            print self.get_player_name(p);
            pprint( self.playerStats[p] )
            print "----"

    def calculate_league_player_ranks(self):
        for i in range(0,9):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_player_ranks(i)

    def calculate_league_avg_ages(self):
        for i in range(0,10):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_average_age(i)

    def print_scoring_settings(self):
        pprint(self.scoringSettings)

    def get_weekly_projections(self, week):
        p = requests.get("https://api.sleeper.app/v1/projections/nfl/regular/2019/" + str(week)).json()
        for i in p:
            print self.get_player_name(i)
            pprint(p[i])
        