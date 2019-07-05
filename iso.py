numb1,numb2=map(str,input().split())
if(len(numb1)!=len(numb2)):
    print("no")
else:
  a=[numb1.count(i) for i in numb1]
  b=[numb2.count(i) for i in numb2]

if(a==b):
    print("yes")
else:
    print("no")
