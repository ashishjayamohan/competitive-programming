t = int(input())
answers = []
for a in range(t):
    line = input().split()
    p = int(line[0])
    f = int(line[1])
    line = input().split()
    sword = int(line[0])
    axe = int(line[1])
    line = input().split()
    weightS = int(line[0])
    weightL = int(line[1])
    counter = 0
    for b in range(sword+1):
        for c in range(axe+1):
            weight = weightS*sword*b + weightL*axe*c
            print(str(weight))
            if(p - weight == 0):
                counter += (b+c)
                sword -= b
                axe -= c
                break
            elif((weight+weightL)>p and (weight+weightS)>p):
                counter += (b+c)
                sword -= b
                axe -= c
                break
            elif(p<weight):
                counter += (b+c)
                sword -= b
                axe -= c
                break
        break
    for d in range(sword+1):
        for e in range(axe+1):
            weight = weightS*sword*d + weightL*axe*e
            print(str(weight))
            if(f - weight == 0):
                counter += (d+e)
                sword -= d
                break
            elif((weight+weightL)>f and (weight+weightS)>f):
                counter += (d+e)
                break
        break
    answers.append(counter)
for i in answers:
    print(i)
