# return the sum of numbers in array, except ignore sections starting
# with 6 and ending with 9 - only add numbers outside of that section.
# Return 0 for no numbers.

def six_nine(arr):
# this function is meant to keep adding numbers except when a 6 appears
    total = 0
    add = True   #by default, keep adding: this triggers the loop
# for each number in array while 'add' is True: do the following:
    for num in arr:
        while add:
# the FIRST loop is triggered: if number not 6, add numbers to total
            if num != 6:
                total += num
                break   #loop ends when addition is made
# if number is 6, stop loop of adding; add = False, SECOND loop starts
            else:
                add = False
# add is now False (or: not add:)
        while not add:
# no addition is made anymore until iteration gets to 9
            if num != 9:
                break
# when the loop reaches nine, the FIRST loop starts again (add = True)
            else:
                add = True

    return total

print(six_nine([3,4,6,7,8,9,2,3,6,7,8,9,4,5]))
