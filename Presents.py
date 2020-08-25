n = int(input())
friends = input().split()
for i in range(n):
    print(friends.index(str(i+1))+1)


