t = int(input())
answer = []
def setmax(array, covered):
    counter = len(array)-1
    num = array[counter]
    while(num in covered):
        counter -= 1
        num = array[counter]
    return counter
def setmin(array, covered):
    counter = 0
    num = array[counter]
    while(num in covered):
        counter += 1
        num = array[counter]
    return counter
for a in range(t):
    line = input().split()
    n = int(line[0])
    k = int(line[1])
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(l) for l in input().split()]
    b.sort()
    finala = list(a)
    finalb = list(b)
    covereda = {-15}
    coveredb = {-15}
    for i in range(k):
        currentmax = setmax(b, coveredb)
        currentmin = setmin(a, covereda)
        covereda.add(a[currentmin])
        coveredb.add(b[currentmax])
        temp = b[currentmax]
        finalb[currentmax] = a[currentmin]
        finala[currentmin] = temp
    sum = 0
    for j in finala:
        sum += j
    answer.append(sum)
for a in answer:
    print(str(a))
