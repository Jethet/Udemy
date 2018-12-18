#Given an integer n, return True if n is within 10 of either 100 or 200

def almost(n):
    list1 = range(90, 111)
    list2 = range(190, 211)
    if n in list1 or n in list2:
        return True

print(almost(35))
print(almost(156))
print(almost(198))
