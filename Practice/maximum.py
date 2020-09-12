t = int(input())
answer = []
for a in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    t1 = arr[len(arr)-1]
    t2 = arr[len(arr)-2]
    t3 = arr[len(arr)-3]
    t4 = arr[len(arr)-4]
    t5 = arr[len(arr)-5]
    l1 = arr[0]
    l2 = arr[1]
    l3 = arr[2]
    l4 = arr[3]
    l5 = arr[4]
    if(min(l1,l2,l3,l4,l5) < 0):
        answer.append(t1*l1*l2*l3*l4)
    else:
        answer.append(t1*t2*t3*t4*t5)
for b in answer:
    print(b)
