num = int(input())
greatest = 0
length = 1
line = [int(i) for i in input().split()]
for i in range(1, len(line)):
    if(length > greatest):
        greatest = length
    if(line[i] >= line[i-1]):
        length += 1
    else:
        length = 1
if(length > greatest):
    greatest = length
print(str(greatest))
