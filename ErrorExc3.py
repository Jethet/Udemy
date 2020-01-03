# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.


def ask():
    while True:
        try:
            number = int(input("Please enter a number."))
            print("The square is", number * number)
            break

        except:
            print("This is input is not correct.")

        else:
            print("Thank you.")

ask()
