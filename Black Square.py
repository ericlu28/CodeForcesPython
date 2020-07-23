c1,c2,c3,c4 = map(int, input().split(' '))
list = input()
total = 0

for i in list:
    if i == '1':
        total += c1
    if i == '2':
        total += c2
    if i == '3':
        total += c3
    if i == '4':
        total += c4

print(total)
    

