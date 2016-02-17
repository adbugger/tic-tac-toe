import users, game
choice = 4
while choice != 3:
    print "1: Create new user"
    print "2: Play game"
    print "3: Exit"
    choice = int(raw_input('Choice? '))
    if choice == 1:
        person = users.User(raw_input('Enter name: '), raw_input('Enter password: '))
        person.createUser()
    elif choice == 2:
        p1 = users.Player()
        while not p1.name:
            p1.verify(raw_input('Verify name player 1: '), raw_input('Verify password: '), 'X')
        p2 = users.Player()
        while not p2.name:
            p2.verify(raw_input('Verify name player 2: '), raw_input('Verify password: '), 'O')
        match = game.Match(p1, p2)
        match.players()
