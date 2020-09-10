t = int(input())
answer = []
for a in range(t):
    line = list(input())
    zero = 0
    one = 0
    for b in line:
        if(b == "0"):
            zero += 1
        else:
            one += 1
    cnt = min(zero, one)
    if(cnt%2==1):
        answer.append("DA")
    else:
        answer.append("NET")
for b in answer:
    print(b)
