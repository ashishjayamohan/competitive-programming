import math
line = input().split()
n = int(line[0])
m = int(line[1])
a = int(line[2])
answer = math.ceil(m/a) * math.ceil(n/a)
print(str(int(answer)))
