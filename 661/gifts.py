t = int(input())
answer = []
def minpoo(c,o, minc, mino):
    return max(c-minc, o-mino)
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
