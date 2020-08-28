line = input().split()
n = int(line[0])
k = int(line[1])
total = 0
num = 0
for i in range(1, n+1):
    total += 5*i
    num += 1
    if(total + k > 240):
        total -= 5*i
        num -= 1
print(str(num))
