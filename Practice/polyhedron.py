n = int(input())
total = 0
for i in range(n):
    temp = input()
    if(temp[0] == "T"):
        total += 4
    elif(temp[0] == "C"):
        total += 6
    elif(temp[0] == "O"):
        total += 8
    elif(temp[0] == "D"):
        total += 12
    else:
        total += 20
print(str(total))
