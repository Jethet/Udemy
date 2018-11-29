#Import random module to use randint (creates random integer)
from random import randint

#generate random integer between 1 and 100
guess_int = randint(1, 100)

print("Welcome to the game. You can enter a number between 1 and 100. \
You will get one of these messages: 1) YOU WON! 2) WARM! 2) COLD! \
Message 2 means you picked a number within 10 values below or above \
the number you must guess. Message 3 means your guess is further away \
from the solution. You can stop anytime by typing 0.\nHave fun!")

while True:
    try:
#the player is asked for a number
        guess = int(input("Please pick a number. "))
#the user can stop any time:
        if guess == 0:
            print("Thank you for playing!")
            break
#the number must be between 1 and 100
        elif guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
#if user guess is equal to random, print YOU WON!
        elif guess == guess_int:
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
#the input has to be an integer
    except ValueError:
        print("Please only enter one number as correct input.")
        continue
