"""
1|2|3
4|5|6
7|8|9
Player uses X or O
"""

def choice_board():
    square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    choice = int(input("Which square do you choose? "))
    if choice in square:
        square[choice] = 'X'
        square.remove(choice)
        print(*square, sep='')


    else:
        print("This is not a valid choice.")



"""
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice = int(input("Which square do you choose? "))
if choice in board:
    if choice == 1:
        print(' X | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n')

board[n] = 'input'  = give position that gets new input
board.remove(choice)
"""
