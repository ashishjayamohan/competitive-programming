line = input().split()
n = int(line[0])
h = int(line[1])
width = 0
line = [int(i) for i in input().split()]
for j in line:
    if(j>h):
        width += 2
    else:
        width += 1
print(str(width))
