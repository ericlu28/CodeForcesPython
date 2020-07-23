events = int(input())
crimes = []
crimes = list(map(int, input().split(' ')))

untreated = 0
policemen = 0

for crime in crimes:
    if crime == -1:
        if policemen > 0:
            policemen -= 1
        else:
            untreated +=1
    if crime > 0:
        policemen += crime

print(untreated)
