spaces = int(input())
steps =0
while(spaces > 0):
    if(spaces >= 5):
        spaces -= 5
        steps += 1
    elif(spaces >= 4):
        spaces -= 4
        steps += 1
    elif(spaces >= 3):
        spaces -= 3
        steps += 1
    elif(spaces >= 2):
        spaces -= 2
        steps += 1
    elif(spaces >= 1):
        spaces -= 1
        steps += 1
print(str(steps))
