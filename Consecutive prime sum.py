s=0
r=10**3
p=[]
sm=[]
x=0
def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
for i in range(2,r):
    if prime(i):
        p.append(i)        
for i in p:
    for j in range(i,r):
        if prime(j):
            for k in range(i,j+1):
                if prime(k):
                    s+=k
                    if prime(s) and s<r:
                        sm.append(s)
print(sm)
ans=max(sm)
print(ans)        
                        
                        
    
