t = int(input())
answer = []
def minpoo(c,o, minc, mino):
    total = 0
    while(c!=0 and o!=0):
        if(c==minc and o==mino):
            return total
        elif(c-1 >= minc and o-1 >= mino):
            total += 1
            c -= 1
            o -= 1
        elif(c-1 >= minc):
            total += 1
            c -= 1
        elif(o-1 >= mino):
            total += 1
            o -= 1
for a in range(t):
    n = int(input())
    line1 = [int(i) for i in input().split()]
    line2 = [int(j) for j in input().split()]
    minc = min(line1)
    mino = min(line2)
    total = 0
    for i in range(n):
        total += minpoo(line1[i], line2[i], minc, mino)
    answer.append(total)
for b in answer:
    print(str(b))
