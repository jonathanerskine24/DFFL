



class test():


    def __init__(self):
        print "init"

        self.table = {}

    def add_to_table(self, x, y, z):
        tempdick = {}
        stats = {}
        stats["posRank"] = y
        stats["CMC"] = z
        # stats["avg"] = w
        tempdick[x] = stats
        self.table.update(tempdick)

    def print_table(self):
        print self.table["Marlon Mack"]["posRank"]


test = test()

test.add_to_table("Christian McCaffrey", 1, 1.0)
test.add_to_table("David Johnson", 9, .654, )
test.add_to_table("Marlon Mack", 10, .603)



test.print_table()

