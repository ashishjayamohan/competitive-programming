n = int(input())
counter = 0
line = list(input())
for i in range(1,len(line)):
    if(line[i] == line[i-1]):
        counter+=1
print(str(counter))
