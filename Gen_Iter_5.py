my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)

# 'gencomp' iterates over a list to compare values to condition and
# generates the values that meet the condition
