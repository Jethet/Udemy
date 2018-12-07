"""
Write a function that returns the number of prime numbers that
exist up to and including a given number:
      count_primes(100) --> 25
By convention, 0 and 1 are not prime
"""
def prime(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True

print(prime(14))
