

# temporarily relocated scoring methods over here
# will probably create a separate class for scoring methods in the future


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