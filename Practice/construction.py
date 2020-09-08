t = int(input())
for i in range(t):
    n,a,b = map(int, input().split())
    s = []
    for j in range(n):
        s.append(chr(97 + (j%b)))
    print(''.join(s))
