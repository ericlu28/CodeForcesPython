n,b,d = map(int, input().split())
oranges = [int(i) for i in input().split()]

waste_total=0
empty_times=0

for orange in oranges:
    if orange<=b:
        waste_total+= orange
        if waste_total>d:
            empty_times+=1
            waste_total=0

print(empty_times)

