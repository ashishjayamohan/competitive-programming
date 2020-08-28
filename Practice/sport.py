n = int(input())
if(n == 0):
    print("0")
else:
    counter = 0
    low = 0
    high = 0
    line = [int(i) for i in input().split()]
    for j in range(0,n):
        if(j == 0):
            low = line[j]
            high = line[j]
        else:
            if(line[j] > high):
                high = line[j]
                counter += 1
            elif(line[j] < low):
                low = line[j]
                counter += 1
    print(str(counter))
