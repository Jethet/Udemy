#3-Write a function that accepts a string and calculates number of upper and lower case letters

def up_low(str):
        up = sum(1 for x in str if x.isupper())
        low = sum(1 for x in str if x.islower())
        return (up, low)


print(up_low('WeLcOmE'))
print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
