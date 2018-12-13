#5-Write a function to multiply all the numbers in a list

def multiply(numbers):
    total = 1
    for num in numbers:
        total *= numbers[num]
    return total

print(multiply([1, 2, 3, -4]))
