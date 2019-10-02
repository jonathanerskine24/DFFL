import json
import requests 
from pprint import pprint

class PlayerNode():

    def __init__(self, name, points):
        self.name = name
        self.data = points
        self.l_child = None
        self.r_child = None



def binary_insert(root, node):
    if root is None:
        root = node
        return root
    else:
        if root.data < node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

        return root

def in_order_print(root):
    if not root:
        # print "None"
        return
    in_order_print(root.l_child)
    if (root.data != -100.0):
        print "{} {}".format(root.name, root.data)
    in_order_print(root.r_child)

class PlayerSorter():
    def __init__(self):

        # load player data file
        with open("playerMap.json", 'r') as f:
             self.playerData = json.load(f)

        #load player stats file
        with open("playerStatsMap.json", "r") as f:
            self.playerStats = json.load(f)

        self.QB_root = None
        self.WR_root = None
        self.RB_root = None
        self.TE_root = None

        self.QB_table = None
        self.WR_table = None
        self.RB_table = None
        self.TE_table = None


    def calculate_ppg(self, playerID):
        try:
            points = self.playerStats[playerID]['pts_half_ppr']
            gp = self.playerStats[playerID]['gp']
            ppg = points / gp
            return ppg
        except: 
            return -100.0


    def sort_position(self, position):
        
        for i in self.playerData:
            if self.playerData[i]['position'] == position:
                player_name = self.playerData[i]['full_name']
                
                if position == "QB":
                    self.QB_root = binary_insert(self.QB_root, PlayerNode(player_name, self.calculate_ppg(i)))
                elif position == "WR":
                    self.WR_root = binary_insert(self.WR_root, PlayerNode(player_name, self.calculate_ppg(i)))    
                elif position == "RB":
                    self.RB_root = binary_insert(self.RB_root, PlayerNode(player_name, self.calculate_ppg(i)))
                elif position == "TE":
                    self.TE_root = binary_insert(self.TE_root, PlayerNode(player_name, self.calculate_ppg(i)))


    def print_in_order(self, position):
        if position == "QB":
            in_order_print(self.QB_root)
        elif position == "WR":
            in_order_print(self.WR_root)
        elif position == "RB":
            in_order_print(self.RB_root)
        elif position == "TE":
            in_order_print(self.TE_root)

    def create_tables(self, position):



    def run_all(self):
        positions = ["QB", "WR", "RB", "TE"]
        for p in positions:
            self.sort_position(p)
        self.create_tables()
        


            



ps = PlayerSorter()
ps.sort_position("WR")
ps.print_in_order("WR")

print "---"

ps.sort_position("RB")
ps.print_in_order("RB")

print "---"

ps.sort_position("QB")
ps.print_in_order("QB")

print "---"

ps.sort_position("TE")
ps.print_in_order("TE")


