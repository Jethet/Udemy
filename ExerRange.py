#2-Write a function that checks whether a number is in a
#given range (inclusive of high and low)

def ran_check(num, low, high):
    if num >= low and num <= high:
        print(num, "is in the range between", low, "and" , high)
    else:
        print(num, "is not in the range between", low, "and", high)

ran_check(5, 2, 7)
ran_check(7, 2, 5)
