line1 = input()
line2 = input()
line3 = input()
ans = True
for i in range(65,91):
    if(line1.count(chr(i))+line2.count(chr(i)) != line3.count(chr(i))):
        ans = False
        break
if(ans):
    print("YES")
else:
    print("NO")
