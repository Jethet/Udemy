# one.py
"""
  __name__ is a built-in variable in Python
When you run your file (example: one.py), __name__ is assigned
automatically if you run your script directly: this means with
   $python3 one.py   on the command line, Python will automatically assign
 __name__ to __main__ as follows:
  __name__ == "__main__"
This means you can use an if statement:
 if __name__ == "__main__":
                  .... (code)

It means the .py file is being run directly because this evaluates to True.
"""
# With all functions and classes defined at level 0, you will see this
# at the bottom of someone's code:

if __name__ == "__main__":
    myfunc1()
    myfunc2()
    myfunc3()
    # etc. etc.

# This means that all code will be executed.
