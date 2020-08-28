t = int(input())
answer = []
ans = []
counter = 0
for a in range(t):
    counter = 0
    n = int(input())
    ans = [0 for d in range(n)]
    line = list(input())
    for b in range(len(line)-n+1):
        current = [line[c] for c in range(b, b+n)]
        #print(current)
        check = int(ans[counter])|int(current[counter])
        # print(current[counter])
        if(str(check) == current[counter]):
            ans[counter] = current[counter]
            counter += 1
        else:
            while(str(check) != current[counter]):
                counter += 1
                check = ans[counter]|int(current[counter])
    answer.append(''.join(map(str, ans)) )
for i in answer:
    print(i)
