n = int(input())
wires=[int(i) for i in input().split()]
m = int(input())
for i in range(0, m):
    x, y = map(int, input().split(' '))
    x=x-1
    if x != 0:
        wires[x-1] += y-1
    if x != n-1:
        wires[x+1] += wires[x] - y
    wires[x] = 0

for j in range(0, n):
    print(wires[j])

