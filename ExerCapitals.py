#Write a function that capitalizes the first and fourth letters of a name

def cap1_4(name):
    cap_letter = name.split()
    for letter in cap_letter:
        cap_letter = letter[0].capitalize() + letter[3].capitalize()
        print(''.join(cap_letter))

cap1_4('macdonald')
