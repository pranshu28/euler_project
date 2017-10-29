import math
r=10**3
def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
p=[]
for i in range(2,r):
    if prime(i):
        p.append(i)
def oddcomp(n):
    k=0
    for i in range(2,n):
        if n%i==0 and n%2==1:
            k=1
    if k==0:
        return False
    else:
        return True
c=[]
ans=0
for i in range(2,r):
    if oddcomp(i):
        c.append(i)
for a in c:
    k=0
    for x in range(1,1000):
        if prime(a-2*x*x):
            k=1
        else:
            continue
    if k==0:
        ans=a
        break
    else:
        continue
print(x,a,ans)





