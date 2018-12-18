def almost(n):
    if abs(n) in range (90, 110) or abs(n) in range(190, 210):
        return True

print(almost(95))
print(almost(125))
print(almost(201))
