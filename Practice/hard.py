n = int(input())
if(n == 0):
    print("1")
elif(n%4 == 0):
    print("6")
elif(n%4 == 3):
    print("2")
elif(n%4 == 2):
    print("4")
else:
    print("8")
