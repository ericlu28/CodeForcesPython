n = int(input())
counter = 0
for i in range(n):
    x,y,z = map(int, input().split(" "))
    sum = x+y+z
    if sum >= 2:
        counter += 1
 
print(counter)