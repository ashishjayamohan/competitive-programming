n = int(input())
array = {}
answers = []
for a in range(n):
    line = input()
    if(line in array):
        answers.append(line+str(array[line]))
        array[line] += 1
    else:
        answers.append("OK")
        array[line] = 1
for b in answers:
    print(b)
