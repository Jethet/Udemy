"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less
than or equal to 21, return their sum.
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""
def blackjack(x, y, z):
    if sum((x, y, z)) <= 21:
        return sum((x, y, z))
    elif sum((x, y, z)) > 21 and 11 in (x, y, z):
        return sum((x, y, z)) - 10
    else:
        return 'BUST'

print(blackjack(5, 7, 9))
print(blackjack(15, 6, 11))
print(blackjack(9, 9, 9))
