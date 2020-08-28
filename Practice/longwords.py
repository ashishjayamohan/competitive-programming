number = int(input())
for i in range(number):
    current = input()
    if(len(current)>10):
        print(current[0]+str(len(current)-2)+current[len(current)-1])
    else:
        print(current)
