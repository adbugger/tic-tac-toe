class cell(object):
    def __init__(self, state = "_"):
        self.state = state
class match(cell):
    def __init__(self):
        self.board = []
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
