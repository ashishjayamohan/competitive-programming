n = int(input())
line = input()
ans = ""
for j in range(line.count("n")):
    ans += "1 "
for j in range(line.count("z")):
    ans += "0 "
print(ans)
