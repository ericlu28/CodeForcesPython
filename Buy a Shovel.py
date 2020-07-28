a,b = map(int, input().split())
shovels = 0
shovel_price = a

while a%10 != b and a%10 != 0:
    a += shovel_price
    shovels+=1

print(shovels + 1)