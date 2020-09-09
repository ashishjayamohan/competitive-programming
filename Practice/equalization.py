t = int(input())
answer = []
for a in range(t):
    count1 = [0 for i in range(26)]
    count2 = [0 for j in range(26)]
    line1 = set(list(input()))
    line2 = set(list(input()))
    ans = False
    for j in line1:
        if(j in line2):
            ans = True
            break
    if(ans):
        answer.append("YES")
    else:
        answer.append("NO")
for b in answer:
    print(b)
