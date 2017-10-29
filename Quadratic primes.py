def prime(n):
    k=0
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
r=1000
y=0
c=0
d=0

for a in range(-r,r):
    for b in range(r):
        if prime(b) and (b<y or b<-1600-40*a):
            t,n=1,1
            while prime((n**2)+(a*n)+b) and ((n**2)+(a*n)+b)>0:
                print(t,n,a,b,(n**2)+(a*n)+b)
                t+=1
                n+=1
            if t>y:
                y=t
                c=a
                d=b
print(y,c,d,"-",c*d)            
        
