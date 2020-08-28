check = ["h","e","l","l","o"]
current = 0
line = list(input())
for i in line:
    if(current<len(check) and i == check[current]):
        current += 1
if(current == 5):
    print("YES")
else:
    print("NO")
