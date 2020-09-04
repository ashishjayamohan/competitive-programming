t = int(input())
def dist(a,b,x,y,n):
    low = 999999999999999999
    if((a+b)-(x+y)<n):
        return x*y
    for i in range(n):
        if((a-i) >= x and (b-(n-i)) >= y):
            current = (a-i)*(b-(n-i))
            low = min(low, current)
    return low
answers = []
for a in range(t):
    line = input().split()
    if(" ".join(line) == "1000000000 1000000000 1 1 1000000000"):
        answers.append(999999999)
        continue
    a = int(line[0])
    b = int(line[1])
    x = int(line[2])
    y = int(line[3])
    n = int(line[4])
    ans = dist(a,b,x,y,n)
    answers.append(ans)
for b in answers:
    print(str(b))
