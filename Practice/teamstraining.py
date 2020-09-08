line = input().split()
n = int(line[0])
m = int(line[1])
type1 = 0
type2 = 0
max = 0
for i in range(m):
    type1 = m
    type2 = min(m-2*i, n-i)
    if(type1+type2 > max):
        max = type1+type2
print(max)
