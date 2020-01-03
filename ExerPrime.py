"""
Write a function that returns the number of prime numbers that
exist up to and including a given number:
      count_primes(100) --> 25
By convention, 0 and 1 are not prime
"""
def prime(num):
#check for 0 or 1 input:
    if num < 2:
        return 0
#because 2 is the first prime number, the prime_list starts with value 2.
    prime_list = [2]
#couter going up to the input value num
    x = 3
# x is going through every number up to input num
    while x <= num:
#check if x is prime:
#start at 3, stop at x and take steps of 2 because even numbers over 2
# are never primes.
        for y in range(3, x, 2):
            if x % y == 0:
#skip even numbers (they are not primes)
                x += 2
                break
        else:
            prime_list.append(x)
#skip even numbers (they are not primes)
            x += 2
    print(prime_list)
    return len(prime_list)


print(prime(25))
