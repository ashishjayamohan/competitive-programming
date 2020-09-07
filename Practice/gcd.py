t = int(input())
answer = []
for a in range(t):
    n = int(input())
    if(n>2):
        answer.append(n//2)
    else:
        answer.append(1)
for b in answer:
    print(str(b))
