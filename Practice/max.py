t = int(input())
answer = []
for a in range(t):
    line = [int(i) for i in input().split()]
    line.sort()
    if(line[1] != line[2]):
        answer.append("NO")
    else:
        reg = "YES\n"+str(line[0]) + " " + str(line[0]) + " " + str(line[2])
        answer.append(reg)
for b in answer:
    print(b)
