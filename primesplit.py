numb1,numb2=map(int,input().split())
for i in range(numb1+1,numb2):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
    print(i,end=" ")
