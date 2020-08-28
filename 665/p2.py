t = int(input())
answer = []
for a in range(t):
    sumv = 0
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    m = min(x[0],y[2])
    x[0] -= m
    y[2] -= m

    m = min(x[1],y[0])
    x[1] -= m
    y[0] -= m

    m = min(x[2],y[1])
    x[2] -= m
    y[1] -= m
    sumv += 2 * m
    x = 2 * min(x[1],y[2])
    sumv = sumv - x
    answer.append(sumv)
for b in answer:
    print(b)
