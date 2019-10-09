import json
import requests 
from pprint import pprint
import PlayerSorter

class PlayerParser():

    def initialize_userID_map(self, league_id):
        t = requests.get("https://api.sleeper.app/v1/league/{}/users".format(league_id)).json()
        self.userIDmap = {}
        for x in t:
            self.userIDmap[x['user_id']] = x['display_name']
            # print "{} --> {}".format(x['user_id'], x['display_name'])
        return

    def get_league_info(self, league_id):
        self.leagueInfo = requests.get("https://api.sleeper.app/v1/league/" + league_id).json()
        self.scoringSettings = self.leagueInfo["scoring_settings"]
        self.initialize_userID_map(league_id)
        return


    def get_roster_info(self, league_id):
        self.rosterInfo = requests.get("https://api.sleeper.app/v1/league/" + league_id + "/rosters").json()
        return

    def get_username(self, user_id):
        return self.userIDmap[str(user_id)]

    def init_player_table(self):
        self.ps = PlayerSorter.PlayerSorter()
        self.ps.run_all()
        self.playerTable = self.ps.get_player_table()

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

        self.init_player_table()

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

    def get_player_position(self, playerID):
        return self.playerData[playerID]['position']

    # methods for analyizing teams

    # methods for calculating things about a single team

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
        print playerIDs

    def get_team_CMC_value(self, teamID):
        totalCMCval = 0
        playerIDs = self.rosterInfo[teamID]['players']
        for p in playerIDs:
            if ((self.get_player_position(p) != "K") and (self.get_player_position(p) != "DEF")):
                player_name = self.get_player_name(p)
                try:
                    totalCMCval = totalCMCval + self.playerTable[player_name]['CMC']
                except:
                    pass
        return totalCMCval

    def get_team_starting_CMC_value(self, teamID):
        totalCMCval = 0
        playerIDs = self.rosterInfo[teamID]['starters']
        for p in playerIDs:
            if ((self.get_player_position(p) != "K") and (self.get_player_position(p) != "DEF")):
                player_name = self.get_player_name(p)
                try:
                    totalCMCval = totalCMCval + self.playerTable[player_name]['CMC']
                except:
                    pass
        return totalCMCval

    def get_team_avg_ranks(self, teamID):
        playerIDs = self.rosterInfo[teamID]['starters']
        WR_total = 0
        RB_total = 0
        WR_count = 0
        RB_count = 0
        for p in playerIDs:
            if (self.get_player_position(p) == 'RB'):
                RB_total = RB_total + self.playerTable[self.get_player_name(p)]['posRank']
                RB_count = RB_count + 1
            if (self.get_player_position(p) == 'WR'):
                WR_total = WR_total + self.playerTable[self.get_player_name(p)]['posRank']
                WR_count = WR_count + 1
        RB_avg = RB_total / float(RB_count)
        WR_avg = WR_total / float(WR_count)
        print "RB Avg: {:.2f} WR Avg: {:.2f}".format(RB_avg, WR_avg)


    # Methods for calculating league wide stats

    def calculate_league_player_ranks(self):
        for i in range(0,9):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_player_ranks(i)

    def calculate_league_avg_ages(self):
        for i in range(0,10):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_average_age(i)

    def calculate_league_CMCs(self):
        for i in range(0, 10):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print self.get_team_CMC_value(i)

    def calculate_league_starting_CMCs(self):
        for i in range(0,10):
            print self.get_username(self.rosterInfo[i]['owner_id'])
            print "{:.4f}".format(self.get_team_starting_CMC_value(i))

    def calculate_league_pos_ranks(self):
        for i in range(0,10):
            print self.get_username(self.rosterInfo[i]["owner_id"])
            self.get_team_avg_ranks(i)

    def print_scoring_settings(self):
        pprint(self.scoringSettings)

    # Misc Methods

    def get_weekly_projections(self, week):
        p = requests.get("https://api.sleeper.app/v1/projections/nfl/regular/2019/" + str(week)).json()
        for i in p:
            print self.get_player_name(i)
            pprint(p[i])

    def print_lists(self):
        self.ps.print_all()