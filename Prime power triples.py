def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
l=[]
r=50000000
"""1097343"""
for i in range(2,int(r**.5)):
    if prime(i):
        l.append(i)
c=0
for i in l:
    if i<(r**.5):
        for j in l:
            if j<(r**(1/3)):
                for k in l:
                    if k<r**.25:
                        if (i**2+j**3+k**4)<r:
                            c+=1
                            print(i,j,k,i**2+j**3+k**4)
print(c)
                
            
