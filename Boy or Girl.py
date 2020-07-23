string = input()
unique = []
for char in string:
    if char not in unique:
        unique.append(char)
n = len(unique)

if n % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")