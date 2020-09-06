t = int(input())
answer = []
for a in range(t):
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    if(n == 0):
        answer.append(0)
    else:
        answer.append(min(2,n-1)*m)
for b in answer:
    print(str(b))
