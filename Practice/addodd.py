t = int(input())
answer = []
for a in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    if(b>a):
        if((b-a)%2==1):
            answer.append(1)
        else:
            answer.append(2)
    elif(b==a):
        answer.append(0)
    else:
        if((a-b)%2==0):
            answer.append(1)
        else:
            answer.append(2)
for b in answer:
    print(str(b))
