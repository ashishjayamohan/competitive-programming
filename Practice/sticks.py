line = input().split()
n = int(line[0])
m = int(line[1])
ans = min(n,m)
if(ans%2==0):
    print("Malvika")
else:
    print("Akshat")
