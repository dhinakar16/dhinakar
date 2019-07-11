    
numbr=int(input())
lst=[]
for i in range(0,numbr):
   lst1=input()
   lst.append(lst1)
lst2=[]
for i in zip(*lst):
 if(i.count(i[0])==len(i)):
  lst2.append(i[0])
 else:
  break
print(''.join(lst2))
