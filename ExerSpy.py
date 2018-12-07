#Write a function that takes in a list of integers and returns
# True if it contains 007 in order
def spy(values):
    spylist = [0, 0, 7, 'x']
#you iterate through all values to check if the value matches
#  the value in position 0 in spylist. If it does match (because
#  it is a 0 or 7) you delete that value from spylist
    for num in values:
        if num == spylist[0]:
            spylist.pop(0)
# if numbers are popped off spylist, 'x' is left and
#   then the list has length of 1, len(spylist)== 1 is True if only 'x'
#   is left, False if one or more of 0,0,7 still present (not popped).
    return len(spylist) == 1



print(spy([7,2,0,3,4,0]))
