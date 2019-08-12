import json
import requests 
from pprint import pprint

class PlayerParser():

    def __init__(self):
        # get scoring settings
        r = requests.get("https://api.sleeper.app/v1/league/386975772876750848").json()
        self.scoringSettings = r["scoring_settings"]

        # load player data file
        with open("playerMap.json", 'r') as f:
             self.playerData = json.load(f)
    
    def get_player_name(self, playerID):
        if self.playerData[playerID]['position'] != "DEF":
            return self.playerData[playerID]['full_name']
        else:
            return self.playerData[playerID]['last_name'] + " D/ST"

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


