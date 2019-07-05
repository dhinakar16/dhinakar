dat = input()
dl = list(dat)
for i in range(0,len(dl),2) :
    dl[i],dl[i+1]=dl[i+1],dl[i]
move = ''.join(dl)
print(move)
