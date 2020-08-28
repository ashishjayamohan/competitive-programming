#32 diff
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
line = Convert(input())
line[0] = line[0].upper()
print("".join(line))
