dt1,dt2=input().split()
c=abs(len(dt2)-len(dt1))
for g in range(len(dt1)):
  if(len(dt2)==1 and dt2[g] in dt1):
    break
  if(dt1[g]!=dt2[g]):
    c=c+1
print(c)
