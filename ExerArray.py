#Given a list of ints, return True if the array contains
#  a 3 next to a 3 somewhere.

def has_3(nums):
    if '3,3' in nums or 33 in nums:
        return True

print(has_3([1,3,7,3,8]))
