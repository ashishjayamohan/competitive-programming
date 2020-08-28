num = int(input())
counter = 0
for i in range(num):
    line = input().split()
    if(int(line[1])-int(line[0])>=2):
        counter+=1
print(str(counter))
