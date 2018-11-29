#function with 2 integers: if sum is 20, return True; otherwise False

def is_Twenty(x, y):
    if x * y == 20:
        print("True")
        return True

    else:
        print("False")
        return False

is_Twenty(5, 13)
is_Twenty(10, 2)
