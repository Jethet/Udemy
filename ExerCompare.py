#Compare two values: if even, return smallest; if odd, return biggest.

def compare(x, y):
    try:
        if True:
            x % 2 == 0 and y % 2 == 0
            print(min(x, y))
        elif False:
            print(max(x, y))
#the exception is meant to prevent raising an error in case of characters
    except NameError:
        print("Please enter numbers only.")

compare(2, 6)
compare(7, 9)
compare(7, 7)
compare(7, a)    #this raises a NameError so the exception does not work
