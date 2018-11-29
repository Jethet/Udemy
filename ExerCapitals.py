#Write a function that capitalizes the first and fourth letters of a name

def cap1_4(name):
    return name[0].capitalize() + name[1:3] + name[3].capitalize()\
            + name[4:]

print(cap1_4('macdonald'))
