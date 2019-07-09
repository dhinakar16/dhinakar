numbr=int(input())
temp=list(map(int,input().split()))
temp.sort()
temp.reverse()
if temp[0]==0:
    print(0)
else:
  for i in temp:
      print(i,end='')
