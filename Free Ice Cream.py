n, x = map(int, input().split())
distressed=0
while n>0:
    n-=1
    sign, amount = input().split(' ')
    amount = int(amount)
    if sign == '+':
        x += amount
    else:
        if x<amount:
            distressed+=1
        else:
            x-=amount

print(x, distressed)
