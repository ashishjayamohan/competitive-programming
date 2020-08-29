line = input().split()
n = int(line[0])
m = int(line[1])
day = 1
total = 2*n
while(total > 0):
    total -= 2
    if(day % m == 0):
        total += 2
    day += 1
print(str(day-1))
