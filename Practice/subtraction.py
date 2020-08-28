def subtract(number):
    if(number % 10 == 0):
        return number/10
    else:
        return number - 1
line = input().split()
n = int(line[0])
k = int(line[1])
for i in range(k):
    n = subtract(n)
print(str(int(n)))
