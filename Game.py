"""
#Import random module to use randint (creates random integer)
from random import randint

#generate random integer between 1 and 100
guess_int = randint(1, 100)
"""
guess_int = 24

while True:
    guess = int(input("Please pick a number. "))
    if guess_int + 10 < guess or guess_int - 10 < guess:
        print("WARM!")
    
        print("COLD!")
    else:
        print("Whatever")
