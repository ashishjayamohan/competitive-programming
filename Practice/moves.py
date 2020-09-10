t = int(input())
answer = []
for a in range(t):
    n = int(input())
    ans = int(8*(((n)*(n+1)*(2*n+1))/6))
    answer.append(ans)
for b in answer:
    print(str(b))
