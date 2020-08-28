line = input().split()
n = int(line[0])
k = int(line[1])
lst = input().split()
interArray = [int(i) for i in lst]
counter = 0
score = interArray[k-1]
for i in interArray:
    if(i > 0 and i >= score):
        counter += 1
print(str(counter))
