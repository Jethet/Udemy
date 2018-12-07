#return the sum of numbers in array, except ignore sections starting
#  with 6 and ending with 9 - only add numbers outside of that section.
#  Return 0 for no numbers.

def six_nine(arr):
#determine position of 6 and 9
    x = arr.index(6)
    y = arr.index(9)

#check if there is a 6 (which means there is also a 9)
    if arr.index(6) == 0:
        return 0
    else:
        result = sum(arr[0:x] + arr[(y+1):])
        return result

print(six_nine([1,3,5,6,7,9,11]))
