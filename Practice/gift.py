num = int(input())
line = input().split()
array = list(range(num))
for i in range(len(line)):
    array[int(line[i])-1] = i+1
for i in range(len(array)):
    if(i != len(array)-1):
        print(str(array[i]),end=" ")
    else:
        print(str(array[i]))
