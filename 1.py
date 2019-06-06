a=input()
a=int(a)
L1=[]
for j in range(0,a):  
    a1=input()
    L1.append(a1)
Z1=[]
for j in zip(*L1):
    if j.count(j[0])==len(j): 
        Z1.append(j[0])
    else:
        break
print(''.join(Z1))
