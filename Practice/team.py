# Not finished
rows = int(input())
array = [[0 for x in range(3)] for y in range(rows)]
for i in range(rows):
    line = [float(i) for i in input().split()]
    for j in range(3):
        array[i][j] = int(line[j])
totalcount = 0
for k in range(rows):
    counter=array[k][0] +array[k][1] +array[k][2]
    if(counter >= 2):
        totalcount += 1
print(str(totalcount))
#bur
