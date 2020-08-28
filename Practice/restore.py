line = [int(i) for i in input().split()]
total = max(line)
answer = ""
for j in line:
    if(total - j != 0):
        answer += (str(total -j) + " ")
print(answer)
