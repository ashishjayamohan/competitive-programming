n = int(input())
def factorial(num):
    if(num <= 1):
        return 1
    else:
        return num*factorial(num-1)
ans = int((factorial(2*n-2))/(factorial(n-1)*factorial(n-1)))
print(str(ans))
