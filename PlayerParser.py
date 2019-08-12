import json
import requests 
from pprint import pprint

class PlayerParser():

    def initialize_userID_map(self):
        t = requests.get("https://api.sleeper.app/v1/league/386975772876750848/users").json()
        self.mynewdict = {}
        for x in t:
            self.mynewdict[x['user_id']] = x['display_name']
        return


    def __init__(self):

        # get league info
        self.leagueInfo = requests.get("https://api.sleeper.app/v1/league/386975772876750848").json()
        self.scoringSettings = self.leagueInfo["scoring_settings"]

        # get roster info
        self.rosterInfo = requests.get("https://api.sleeper.app/v1/league/386975772876750848/rosters").json()

        # get userID map
        self.initialize_userID_map()

        # load player data file
        with open("playerMap.json", 'r') as f:
             self.playerData = json.load(f)
    
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

    def get_QB_Score(self, playerID):
        pass

    def get_WR_RB_TE_Score(self, playerID):
        pass

    def get_K_Score(self, playerID):
        pass

    def getPlayerScore(self, playerID):
        playerPos = self.playerData[playerID]['position']

        if playerPos == "QB":
            resp = get_QB_Score(playerID)
        elif (playerPos == "WR") or (playerPos == "RB") or (playerPos == "TE"):
            resp = get_WR_RB_TE_Score(playerID)
        elif playerPos == "K":
            resp = get_K_Score(playerID)

        return resp

    # methods for analyizing teams

    def get_username(self, user_id):
        return self.mynewdict[str(user_id)]

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

    def calculate_league_avg_ages(self):
        for i in range(0,10):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_average_age(i)

