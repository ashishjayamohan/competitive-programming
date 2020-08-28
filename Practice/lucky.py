n = int(input())
lucky = False
for i in range (1, n + 1, 1):
    number_string = str(i)
    isLucky = True
    for k in range (0, len(number_string), 1):
        if number_string[k] != '4' and number_string[k] != '7':
            isLucky = False
    if n % i == 0 and isLucky == True:
        lucky = True

if lucky == True:
    print ("YES")
else:
    print ("NO")
