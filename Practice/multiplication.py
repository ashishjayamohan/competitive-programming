line = input().split()
n = int(line[0])
x = int(line[1])
count = 0
for a in range(n):
    if(x%(a+1) == 0 and x/(a+1) <= n):
        count += 1
print(count)
