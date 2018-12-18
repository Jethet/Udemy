#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5
#representation of that letter

def print_big(letter):
    print("  ", letter, "\n", letter," ",letter,"\n",letter * 5,"\n",letter, " ", letter,"\n",letter, " ",letter)

print_big('*')
