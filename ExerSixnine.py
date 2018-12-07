#return the sum of numbers in array, except ignore sections starting
#  with 6 and ending with 9 - only add numbers outside of that section.
#  Return 0 for no numbers.

def six_nine(arr):
    x = arr.index(6)
    y = arr.index(9)
#check if there is a 6 (which means there is also a 9)
    while True:
        result = sum(arr[0:x] + arr[(y+1):])
        return result
        break
    else:
        return 0

print(six_nine([1,3,5]))
