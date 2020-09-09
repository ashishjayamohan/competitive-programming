def comp(a,b):
    if(sum(list(a))%2 == sum(list(b))%2):
        return True
    else:
        return False
a = [int(i) for i in list(input())]
b = [int(i) for i in list(input())]
count = 0
for j in range(0, len(a)-len(b)):
    samp = a[j:j+len(b)-1]
    if(comp(samp, b)):
        count += 1
print(count+1)
