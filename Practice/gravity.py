n = int(input())
array = [int(i) for i in input().split()]
array.sort()
array = [str(k) for k in array]
print(" ".join(array))
