n = int(input())
line = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
num = 1
while(num != n):
    hold = line[0]
    line.pop(0)
    line.append(hold)
    line.append(hold)
    num += 1
print(line[0])
