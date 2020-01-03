#Given a list of ints, return True if the array contains
#  a 3 next to a 3 somewhere

def has_3(nums):
    if 33 in nums or [3, 3] in nums:
        return True

print(has_3([1,33,7,3,8]))
print(has_3([1,43, 35, 7]))
