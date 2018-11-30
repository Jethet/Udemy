#Compare two values: if two values are even, return smallest; if odd, return biggest.

def compare(x, y):
    try:
        if x % 2 == 0 and y % 2 == 0:
            print(min(x, y))
        else:
            print(max(x, y))
    #the exception is meant to prevent raising an error in case of characters
    except Exception as e:
        print("Please enter numbers only.", e)

compare(2, 6)
compare(7, 9)
compare(7, 7)
compare('d', 'a')
