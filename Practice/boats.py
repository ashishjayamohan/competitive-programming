t = int(input())
answer = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    line.sort()
    left = 0
    right = len(line)-1
    ans = 0
    for s in range(2,2*n):
        cur = 0
        for i in range(1, int((s+1)/2)):
            if(s-i > n):
                continue
            cur += min(line[i], line[s - i])
        if (s % 2 == 0):
            cur += line[int(s / 2)] / 2
        ans = max(ans, cur)
    answer.append(ans)
for b in answer:
    print(str(int(b)))
