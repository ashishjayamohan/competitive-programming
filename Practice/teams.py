line = input().split()
n = int(line[0])
k = int(line[1])
line = [int(i) for i in input().split()]
counter = 0
for j in line:
    if(5 - j >= k):
        counter += 1
print(str(counter//3))
