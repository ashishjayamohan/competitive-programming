line = input().split()
n = int(line[0])
d = int(line[1])
line = [int(i) for i in input().split()]
line.sort()
m = int(input())
count = 0
for a in range(m):
    if(a < len(line)):
        count += line[a]
    else:
        count -= d
print(count)
