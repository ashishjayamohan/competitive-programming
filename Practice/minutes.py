t = int(input())
answer = []
for a in range(t):
    line = input().split()
    h = int(line[0])
    m = int(line[1])
    ans = ((24-h-1)*60 + 60-m)
    answer.append(ans)
for b in answer:
    print(str(b))
