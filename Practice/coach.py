t = int(input())
answer = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    line.sort()
    result = line[n-1] - line[0]
    for i in range(n):
        for j in range(i+1, n):
            result = min(result, line[j]-line[i])
    answer.append(result)
for b in answer:
    print(str(b))
