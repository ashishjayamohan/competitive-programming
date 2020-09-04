t = int(input())
answer = []
for a in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    if(a==b):
        answer.append(0)
    else:
        ans = 0
        if(abs(a-b)%10 == 0):
            ans = abs(a-b)//10
        else:
            ans = abs(a-b)//10
            ans += 1
        answer.append(ans)

for b in answer:
    print(str(b))
