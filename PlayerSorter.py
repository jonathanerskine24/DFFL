import json
import requests 
from pprint import pprint

rank = 1

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

        self.playerTable = {}


    def in_order_print(self, root):
        global rank
        if not root:
            return
        self.in_order_print(root.l_child)
        if (root.data != -100.0):
            print "{} {} {} {}".format(rank, root.name, root.data,  root.data / 28.82)
            rank = rank + 1
        self.in_order_print(root.r_child)

    def add_to_table(self, root):
        global rank
        if not root:
            return
        self.add_to_table(root.l_child)
        if (root.data != -100.0):
            temp = {}
            stats = {}
            stats["posRank"] = rank
            stats["avg"] = root.data
            stats["CMC"] = root.data / 28.82
            temp[root.name] = stats
            self.playerTable.update(temp)
            rank = rank + 1
        self.add_to_table(root.r_child)

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
        global rank
        if position == "QB":
            rank = 1
            self.in_order_print(self.QB_root)
        elif position == "WR":
            rank = 1
            self.in_order_print(self.WR_root)
        elif position == "RB":
            rank = 1
            self.in_order_print(self.RB_root)
        elif position == "TE":
            rank = 1
            self.in_order_print(self.TE_root)

    def add_pos_to_table(self, position):
        global rank
        if position == "QB":
            rank = 1
            self.add_to_table(self.QB_root)
        elif position == "WR":
            rank = 1
            self.add_to_table(self.WR_root)
        elif position == "RB":
            rank = 1
            self.add_to_table(self.RB_root)
        elif position == "TE":
            rank = 1
            self.add_to_table(self.TE_root)


    def run_all(self):
        positions = ["QB", "WR", "RB", "TE"]
        for p in positions:
            # print "\n {} \n".format(p)
            self.sort_position(p)
            self.add_pos_to_table(p)
    
    def print_all(self):
        positions = ["QB", "WR", "RB", "TE"]
        for p in positions:
            print p
            self.print_in_order(p)

    def test(self):
        print self.playerTable

    def get_player_table(self):
        return self.playerTable


