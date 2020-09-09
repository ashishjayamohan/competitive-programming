t = int(input())
answer = []
for a in range(t):
    val = int(input())
    if(val == 2):
        answer.append(2)
    elif(val%2 == 1):
        answer.append(1)
    else:
        answer.append(0)
for b in answer:
    print(str(b))
