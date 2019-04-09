# Use the iter() function to convert a string 'hello' into an iterator.

s = 'hello'
s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

"""
Same result with:
s = iter(s)
print(next(s))

"""
