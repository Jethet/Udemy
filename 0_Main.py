"""
TicTacToe: 2 players should be able to play the game (both sitting at
the same computer).
The board should be printed out every time a player makes a move.
You should be able to accept input of the player position and then
place a symbol on the board.
"""

#First step is ask player to play and what choice (X or O)
player()

#If the player wants to play: show board and explain choices
create_board()

#If player makes choice, the choice is shown on the board
choice_board()

#To clear screen between games:
print(\n*100)
