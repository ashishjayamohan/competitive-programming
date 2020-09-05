t = int(input())
answers = []
for a in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    x = int(line[2])
    y = int(line[3])
    n = int(line[4])
    ans = 10000000000000000
    for i in range(0,2):
        da = min(n, a-x)
        db = min(n - da, b - y)
        ans = min(ans, (a - da) * (b - db))
        x,y = y,x
        a,b = b,a
    answers.append(ans)
for b in answers:
    print(str(b))
