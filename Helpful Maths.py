string=list(map(int, input().split("+")))
string = sorted(string)
solve=list()
for char in string:
    component=str(char)
    solve.append(component)
print("+".join(solve))
