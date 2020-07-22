def width_road(n,h,heights):
    width = 0
    for height in heights:
        if height > h:
            width += 2
        else:
            width += 1
    return width
 
if __name__ == "__main__":
    n,h = map(int, input().split(" "))
    heights = map(int, input().split(" "))
    print(width_road(n,h,heights))
