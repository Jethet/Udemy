#6-Write a function that checks whether a passed string
# is a palindrome or not

def palindrome(s):
    s = s.replace(' ', '')  #to avoid issues with spaces in strings
    if s == s[::-1]:
        return s

print(palindrome('madam'))
print(palindrome('truth'))
print(palindrome('reder'))
