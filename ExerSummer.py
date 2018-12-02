"""
SUMMER OF '69: Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6 and
extending to the next 9 (every 6 will be followed by at least one 9).
Return 0 for no numbers.
"""
def summer(nums):
    pos6 = nums.index(6)
    pos9 = nums.index(9)
    sumA = sum(nums(1:pos6))
    return sumA

print(summer([1, 4, 6, 10]))
