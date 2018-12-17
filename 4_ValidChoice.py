"""
1|2|3
4|5|6
7|8|9
Player uses X or O
"""

board = {'1':'1 |', '2':' 2 |', '3':' 3\n', '4':'4 |', '5':' 5 |',
        '6':' 6\n', '7':'7 |', '8':' 8 |', '0':' 9\n'}
print(str(board.values()))
"""
for choice in board:
    choice = int(input("What square do you choose? "))
    board[choice] = 'X'
    board.remove(choice)
    print(*board, sep='')

"""
"""
adict.update({key : value})  adds a key and value to dictionary
adict[key] = value		also adds a key and value
del adict[key]			removes key from the dictionary

"""
"""
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choice = int(input("Which square do you choose? "))
if choice in board:
    if choice == 1:
        print(' X | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n')

board[n] = 'input'  = give position that gets new input
board.remove(choice)
"""
