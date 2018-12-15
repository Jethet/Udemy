#7-Write a function to check whether a string is a pangram or not
import string

def ispangram(strl, alphabet=string.ascii_lowercase):
    alphabet = alphabet.split()
    strl = strl.split()
    if alphabet in strl:
        return True
    else:
        return False

print(ispangram('the quick brown fox jumped over the lazy dog'))
print(ispangram('abcdefghijklmnopqrstuvwxyz'))
print(ispangram('abcdefghijklmn'))
