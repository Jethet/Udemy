#The game has two players and they have to choose if they play as X or O

def player():
    start = input("Would you like to play tic tac toe? Choose 1 for yes and 2 for no. ")
    if start == '2':
        print("Game over.")
    else:
        player = input("Choose which player you want to be: 1 for 'X' and 2 for '0'. ")
        if player == '1':
            print("Player X will start: you can choose first.")
        else:
            print("Player X always gets the first turn.")

player()
