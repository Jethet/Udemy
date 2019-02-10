# Error and exception handling - rewrite the following code:

# for i in ['a','b','c']:
#    print(i**2)

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("You cannot perform this operation with a string.")    
