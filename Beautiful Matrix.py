distance = 0
matrix = []
for i in range(5):
   l = list(map(int, input().split()))
   matrix.append(l)
   
for i in range(5):
   for j in range(5):
      if matrix[i][j] == 1:
         x = i
         y = j
 
distance = abs(2-x) + abs(2-y)
print(distance)