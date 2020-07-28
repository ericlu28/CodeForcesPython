a, b = map(int, input().split())
greater = max(a, b)

dice = ["1/6", "1/3", "1/2", "2/3", "5/6", "1/1"]
i = 6 - greater
print(dice[i])