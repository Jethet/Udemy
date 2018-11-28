#Import random module to use randint (creates random integer)
from random import randint

#generate random integer between 1 and 100
guess_int = randint(1, 100)

while True:
    try:
        #the player is asked for a number
        guess = int(input("Please pick a number. "))
        #if user guess is equal to random, print YOU WON!
        if guess == guess_int:
            print("YOU WON!")
            break

        #if user guess is bigger than the random minus 10, print WARM!
        #if user guess is smaller than random plus 10, print WARM!
        elif guess >= (guess_int - 10) and guess <= (guess_int + 10):
            print("WARM!")

        #if user guess is smaller than random minus 10, print COLD!
        #if user guess is bigger than random plus 10, print COLD!
        elif guess < (guess_int - 10) or guess > (guess_int + 10):
            print("COLD!")

    except ValueError:
        print("Please only enter one number as correct input.")
        continue
