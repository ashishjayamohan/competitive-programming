num = int(input())
ans = 0
for i in range(num):
    line = list(input())
    if(line[1] == "-"):
        ans -= 1
    else:
        ans += 1
print(str(ans))
