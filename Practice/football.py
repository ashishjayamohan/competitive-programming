line = list(input())
counter = 0
answer = "NO"
for i in range(1,len(line)):
    if(line[i] == line[i-1] and counter == 0):
        counter += 2
    elif(line[i] == line[i-1] and counter != 0):
        counter+=1
    else:
        counter = 0
    if(counter >= 7):
        answer = "YES"
print(answer)
