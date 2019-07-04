numb1=int(input())
if(numb1%4)==0:
  if(numb1%100)==0:
    if(numb1%400)==0:
      print('yes')
    else:
      print('no')
  else:
     print('yes')
else:
  print('no')
  
