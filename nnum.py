fa1=int(input())
pf=list(map(int,input().split()))[:fa1]
a=len(pf)
l1=[]
for i in range(a):
  b=i+1
  for j in range(b,a):
    if pf[i]==pf[j] and pf[i] not in l1:
      l1.append(pf[i])
l1.sort()
if len(l1)==0:
    print("unique")
else:
    print(*l1,end=' ')
