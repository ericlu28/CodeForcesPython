n = int(input())
magnets = []

for i in range(n):
    magnet = int(input())
    magnets.append(magnet)
changes = 0
for i in range(n-1):
    if magnets[i] != magnets[i + 1]:
        changes += 1
print(changes+1)


