# Problem 1: create a generator that generates the squares of numbers
# up to some number n.

def gensquares(N):
    for x in range(N):
        yield x*x

for x in gensquares(10):
    print(x)
