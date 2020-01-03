# The yield statement is preferable in cases of many values that must
# be iterated over but do not have to be produced all at the same
# time in a list or kept in memory as a list

def mil_val(n):
    for x in range(n):
        yield x ** 3

for number in mil_val(20):
    print(number)
