string = input()
upper = 0
lower = 0
for char in string:
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())