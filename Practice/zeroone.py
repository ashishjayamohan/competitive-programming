n= int(input())
line = input().split()
def cond(arr):
    for j in range(len(arr)-1):
        if(arr[j] != arr[j+1]):
            return False
    return True
while(cond(line) == False):
    for j in range(len(line)-1):
        if(arr[j] != arr[j+1]):
            arr.pop(j)
            arr.pop(j+1)
            break
print(len(line))
