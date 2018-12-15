#7-Write a function to check whether a string is a pangram or not
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram('the quick brown fox jumps over the lazy dog'))
print(ispangram('abcdefghijklmnopqrstuvwxyz'))
print(ispangram('abcdefghijklmn'))
"""
def ispangram(str1, alphabet=string.ascii_lowercase):
    alphabet = alphabet.split()
    str1 = str1.split()
    if alphabet in str1:
        return True
    else:
        return False
        """
