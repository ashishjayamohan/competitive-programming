t = int(input())
answer = []
for a in range(t):
    line = [int(i) for i in input().split()]
    a = line[0]
    b = line[1]
    c = line[2]
    n = line[3]
    if(n<2*(c-b-a)):
        answer.append("YES")
    else:
        answer.append("NO")
for b in answer:
    print(b)
