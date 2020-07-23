n = int(input())
string = input()
counter = 0

for i in range(n-1):
    if string[i] == string[i+1]:
        counter += 1

print(counter)