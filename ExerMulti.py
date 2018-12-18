#5-Write a function to multiply all the numbers in a list

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
# return ends the loop so should be aligned with for (at the end of function),
# otherwise you only get the first iteration of the loop returned.

print(multiply([1, 2, 3, -4]))
