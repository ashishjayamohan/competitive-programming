t = int(input())
answer = []
for a in range(t):
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    ans = (n*m)//2
    if(n*m%2 == 1):
        ans += 1
    answer.append(ans)
for b in answer:
    print(str(b))
