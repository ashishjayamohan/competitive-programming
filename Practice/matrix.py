# |3 - r| + |3 - c|
matrix = [[],[],[],[],[]]
for i in range(5):
    matrix[i] = input().split()
r = 0
c = 0
for j in range(5):
    for k in range(5):
        if(matrix[j][k] == "1"):
            r = j+1
            c = k+1
answer = abs(3-r) + abs(3-c)
print(str(answer))
