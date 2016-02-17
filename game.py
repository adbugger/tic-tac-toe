class cell:
    def __init__(self, state = "_"):
        self.state = state

class Match:
    def __init__(self, p1, p2):
        self.board = []
        self.p1 = p1
        self.p2 = p2
        for i in range(3):
            line = []
            for j in range(3):
                line.append(cell())
            self.board.append(line)
    
    def printBoard(self):
        print " ",
        for col in range(3):
            print col,
        print
        row = 0
        for line in self.board:
            print row, 
            for c in line:
                print c.state,
            row = row+1
            print
    
    def players(self):
        print "Player 1: (X)", self.p1.name
        print "Player 2: (O)", self.p2.name
    
    def writeResult(self, result, playerName = None):
        with open("matches.csv", "a") as rfile:
            rfile.write(self.p1.name + ',' + self.p2.name + ',' + result + ',')
            if result == "win":
                rfile.write(playerName)
            rfile.write('\n')
