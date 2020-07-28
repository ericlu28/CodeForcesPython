stones = list(input())
instructions = list(input())
position = 0
i=0


for j in range(len(instructions)):
    if instructions[j] == stones[i]:
        i+=1

print(i+1)
            