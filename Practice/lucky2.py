def isLucky(number_string):
    isLuckyv = True
    for k in range (0, len(number_string), 1):
        if number_string[k] != '4' and number_string[k] != '7':
            isLuckyv = False
    return isLuckyv
line = list(input())
counter = 0
for i in line:
    if(i == "4" or i == "7"):
        counter += 1
if(isLucky(str(counter))):
    print("YES")
else:
    print("NO")
