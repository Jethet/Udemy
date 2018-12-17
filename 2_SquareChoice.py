#This is the function that asks the player to choose where to tic

def choice_board():
    choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square = int(input("Which square do you choose? "))
    if square in choice:
        print('need function')
    else:
        print("This is not a valid choice.")

choice_board()
