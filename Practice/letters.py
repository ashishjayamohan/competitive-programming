line = set(input().strip("{}").split(", "))
if(len(line) == 1 and '' in line):
    print("0")
else:
    print(str(len(line)))
