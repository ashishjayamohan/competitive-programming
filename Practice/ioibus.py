n = int(input())
arr = []
for a in range(n):
    arr.append(input().split("|"))
answer = False
for j in range(len(arr)):
    if(arr[j][0] == "OO"):
        arr[j][0] = "++"
        answer = True
        break
    elif(arr[j][1] == "OO"):
        arr[j][1] = "++"
        answer = True
        break
if(answer):
    print("YES")
    fin = ""
    for j in arr:
        fin += j[0] + "|" + j[1] + "\n"
    print(fin)
else:
    print("NO")
