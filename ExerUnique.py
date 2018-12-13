#4-Write a function that takes a list and returns a new list
#with unique elements of the first list
"""
def unique_list(lst):
    new_lst = []
    for x in lst:
        if x not in new_lst:
            new_lst.append(x)
        return new_lst
"""
def unique_list(lst):
    set_lst = set(lst)
    new_lst = list(set_lst)
    return new_lst

print(unique_list([1,1,1,1,2,2,3,3,3,4,5]))
