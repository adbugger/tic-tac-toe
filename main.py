import users
choice = 4
while choice != 3:
    print "1: Create new user"
    print "2: Play game"
    print "3: Exit"
    choice = int(raw_input('Choice? '))
    if choice == 1:
        users.User(raw_input('Enter name: '), raw_input('Enter password: '))
    elif choice == 2:
        p1 = users.Player(raw_input('Verify name: '), raw_input('Verify password: '), 'X')
        p2 = users.Player(raw_input('Verify name: '), raw_input('Verify password: '), 'O')
