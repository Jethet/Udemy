# Create a generator that yields 'n' random numbers between a low
# and high number (these are inputs). Use the random library.

import random

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)

for num in rand_num(1, 10, 12):
    print(num)
