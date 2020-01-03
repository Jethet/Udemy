#Write a function takes a two-word string and returns True if
#both words begin with same letter

def first_letter(x):

#returns a list with the two words in the string
    word_list = x.split()
    if word_list[0][0] == word_list[1][0]:
        print("The first letters are the same.")
        return True
    else:
        print("The first letters are not the same.")
        return False

first_letter("vandaag niet")
first_letter("allday allways")
