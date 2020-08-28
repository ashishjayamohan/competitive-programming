def floor(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1
line = input().split()
m = int(line[0])
n = int(line[1])
answer = floor(m*n*0.5)
print(str(answer))
