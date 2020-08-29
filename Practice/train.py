line = input().split()
n = int(line[0])
m = int(line[1])
a = int(line[2])
b = int(line[3])
if(b/m > a):
    print(a*n)
else:
    p = 1
    if n % m == 0:
        p = 0
    f = b * ((n // m) + p)
    s = b * (n // m) + a * (n - m * (n // m))
    print(str(min(f,s)))
