card = list(input())
ports = [list(i) for i in input().split()]
ans = False
for i in ports:
    if(i[0] == card[0] or i[1] == card[1]):
        ans = True
        break
if(ans):
    print("YES")
else:
    print("NO")
