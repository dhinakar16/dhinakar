numbr=int(input())
lst=list(map(int,input().split()))
temp=[]
for i in lst:
	if lst.count(i)>1:
		if i not in temp:
			temp.append(i)
print(*temp)
if len(temp)==0:
  print("unique") 
