c = []
d = []
n = int(input())
games = 0
for i in range(n):
    a, b = map(int, input().split())
    c.append(a)
    d.append(b)

for i in c:
    if i in d:
        games+=d.count(i)

print(games)
