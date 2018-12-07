#Write a function that takes in a list of integers and returns
# True if it contains 007 in order
def spy(values):
    x = 0
    y = 0
    z = 7
    for i in values:
        if x and y and z in values:
            return True
        else:
            return False

print(spy([1, 0, 6, 0, 8, 7]))
