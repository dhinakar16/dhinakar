prim=int(input())
if prim>1:
  for i in range(2,prime):
    if(prim%i==0):
      print ("no")
      break
  else:
    print("yes")
else:
  print("yes")
