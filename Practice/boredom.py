line = input().split()
def factorial(num):
    if(num <= 1):
        return 1
    else:
        return num*factorial(num-1)
a = int(line[0])
b = int(line[1])
print(str(factorial(min(a,b))))
