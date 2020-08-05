n = int(input())

while n>0:
    word=input()
    n-=1
    if len(word)>10:
        print(word[0] + str((len(word)-2)) + word[-1])
    else:
        print(word)