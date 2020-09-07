t = int(input())
answer = []
for a in range(t):
    n = int(input())
    if(n%4 == 0):
        answer.append("YES")
    else:
        answer.append("NO")
for b in answer:
    print(b)
