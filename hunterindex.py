numbr=int(input())
lst=list(map(int,input().split()))
temp=[]
for i in range(numbr):
  if (lst[i]==i):
    temp.append(str(lst[i]))
temp.sort()
if(len(temp)==0):
    print("-1")
else:
    print(" ".join(temp))
