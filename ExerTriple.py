#Given a string, return a string where for every character in the original
# there are three characters

def triple(letters):
    triple = [x * 3 for x in letters]
    return ''.join(triple)

print(triple('paperdoll'))
print(triple('codebar'))
