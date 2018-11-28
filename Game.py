"""
#Import random module to use randint (creates random integer)
from random import randint

#generate random integer between 1 and 100
guess_int = randint(1, 100)
"""
guess_int = 24

while True:
    #the player is asked for a number
    guess = int(input("Please pick a number. "))
    #if user guess is smaller than the random minus 10, print WARM!
    if guess < guess_int - 10:
        print("WARM!")
    #elif guess_int + 10 > guess:
        #print("COLD!")
    else:
        print("YOU WON!")
        break
