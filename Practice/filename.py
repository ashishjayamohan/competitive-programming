n = int(input())
line = input()
counter = 0
while("xxx" in line):
    cur = list(line)
    cur.pop(line.index("xxx"))
    line = "".join(cur)
    counter += 1
print(counter)
