t = int(input())
answers = []
def isRound(num):
    n = str(num)
    ans = True
    if(len(n) == 1):
        return ans
    elif(n[0] != "0" and n.count("0") == len(n)-1):
        return ans
    else:
        return False

    return ans
for a in range(t):
    num = int(input())
    for b in range(num):
        if(isRound(b) == True and isRound(num-b)==True):
            answers.append(str(b) + " " + str(num-b))
            break
for c in answers:
    print(c)
