n = int(input())
cases = [0 for j in range(n)]
for i in range(n):
    line = [int(k) for k in input().split()]
    if(line[0]%line[1] == 0):
        cases[i] = 0
    else:
        cases[i] = line[1] - line[0]%line[1]
for j in cases:
    print(str(j))
