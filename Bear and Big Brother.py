def solve(a, b):
    years = 0
    while a<=b:
        a*=3
        b*=2
        years += 1
    return years
    
if __name__ == "__main__":
    a, b = map(int, input().split(" "))
    print(solve(a, b))