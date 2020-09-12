n=int(input())
count=0
for i in range(n):
  a,b=list(map(int,input().split()))
  if a<b:
    count+=1
if count>0:
  print("Happy Alex")
else:
  print("Poor Alex")
