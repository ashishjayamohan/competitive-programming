origb = list(input())
orig = [x.lower() for x in origb]
answer = ""
for x in range(len(orig)):
    i = orig[x]
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y":
        orig[x] = ""
    else:
        orig[x] = "." + i
    answer += orig[x]
print(answer)
