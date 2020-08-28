line = input().split()
a = int(line[0])
b = int(line[1])
year = 0
while(a<=b):
    year += 1
    a *= 3
    b *= 2
print(str(year))
