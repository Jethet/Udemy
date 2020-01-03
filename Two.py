# two.py

import one

print("TOP LEVEL IN TWO.PY")

one.func()  # execute the function that is in one module

if __name__ == '__main__':
    print("Two.py is being run directly")
else:
    print("Two.py has been imported.")
