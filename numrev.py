numb=int(input())
rever=""
while numb>0:
  lstdigit=numb%10
  rever=rever+str(lstdigit)
  numb=numb//10
print(rever)
