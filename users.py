class User(object):
    def __init__(self, name = '', passw = ''):
        self.name = name
        self._password = passw
    
    def createUser(self):
        ufile = open("users.csv", "a")
        ufile.write(self.name + ',' + self._password + '\n')
        ufile.close()

class Player(User):
    def __init__(self, char = None):
        User.__init__(self)
        self.char = char
    
    def verify(self, name, passw, char):
        with open("users.csv", "r") as ufile:
            line = ufile.readline()
            while line:
                entry = line.split(',')
                if name == entry[0] and passw == entry[1].rstrip('\n'):
                    User.__init__(self, name, passw)
                    self.char = char
                    break
                line = ufile.readline()
            else:
                print "Invlaid login!!!"
