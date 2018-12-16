def choice_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice = int(input("Which square do you choose? "))
    if choice in board:
        print('need function')
    else:
        print("This is not a valid choice.")
