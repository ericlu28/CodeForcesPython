horseshoes = list(map(int, input().split(' ')))
duplicate = 0
duplicate = len(horseshoes) - len(set(horseshoes))

print(duplicate)