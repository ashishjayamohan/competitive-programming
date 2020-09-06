n = int(input())
ans = ""
print(n//2)
if(n%2 == 0):
    for i in range(int(n/2)):
        ans += "2 "
else:
    for i in range(int(n//2)-1):
        ans += "2 "
    ans += "3"
print(ans)
