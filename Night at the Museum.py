string = input().lower()
ascii_list = []
a = 0
counter = a
rotations = 0
for char in string:
    ascii_list.append(ord(char) - 97)

#case for string
for num in ascii_list:
    if abs(num - counter) >= 13:
        rotations += (26 - abs(num - counter))
        counter = num
    else:
        rotations += abs(num-counter)
        counter = num

print(rotations)