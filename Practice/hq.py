line = list(input())
answer = False
for i in line:
    if(i == "H" or i == "Q" or i == "9"):
        answer = True
if(answer == True):
    print("YES")
else:
    print("NO")
