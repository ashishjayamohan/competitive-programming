def notfunc(num):
    if(num == 0):
        return 1
    else:
        return 0
n = int(input())
case = 0
cases = ["I hate that ", "I love that ","I hate it","I love it"]
for i in range(n,0,-1):
    if(i == 1):
        print(cases[case+2] + "")
    else:
        print(cases[case], end="")
    case = notfunc(case)
