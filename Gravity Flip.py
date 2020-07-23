n = int(input())
list = list(map(int, input().split(' ')))
list.sort()
for i in range(n):
    print(list[i], end= " ")
