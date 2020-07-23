n = int(input())
cards = []
cards = list(map(int, input().split(' ')))
s = 0
d = 0
turn = 0

while n > 0:
    if turn == 0:
        if cards[n-1] > cards[0]:
            s+=cards[n-1]
            cards.pop(n-1)
            turn = 1
        else:
            s+=cards[0]
            cards.pop(0)
            turn = 1
    else:
        if cards[n-1] > cards[0]:
            d+=cards[n-1]
            cards.pop(n-1)
            turn = 0
        else:
            d+=cards[0]
            cards.pop(0)
            turn = 0
    n -= 1

print(s, d)
    




