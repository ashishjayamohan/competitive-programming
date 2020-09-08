t = int(input())
answer = []
for a in range(t):
    n = int(input())
    line = [int(i) for i in input().split()]
    numodd = 0
    numeven = 0
    for j in range(len(line)):
        if(j%2 == 0 and line[j] == 1):
            numeven += 1
        elif(j%2 == 1 and line[j] == 1):
            numodd += 1
    line = [str(i) for i in line]
    if(numeven == numodd):
        finala = list(str(int("".join(line))))
        final = " ".join(finala)
        if(len(final) != 0):
            answer.append(str(len(finala)) + "\n" + final)
    elif(numodd > numeven):
        while(numodd > numeven):
            for j in range(len(line)):
                if(j%2 == 1 and line[j] == "1"):
                    line.pop(j)
                    numodd -= 1
                    break
        finala = list(str(int("".join(line))))
        final = " ".join(finala)
        if(len(final) != 0):
            answer.append(str(len(finala)) + "\n" + final)
        else:
            answer.append(str(1) + "\n" + str(0))
    elif(numeven > numodd):
        while(numodd < numeven):
            for j in range(len(line)):
                if(j%2 == 0 and line[j] == "1"):
                    line.pop(j)
                    numeven -= 1
                    break
        finala = list(str(int("".join(line))))
        final = " ".join(finala)
        if(len(final) != 0):
            answer.append(str(len(finala)) + "\n" + final)
        else:
            answer.append(str(1) + "\n" + str(0))
for b in answer:
    print(b)
