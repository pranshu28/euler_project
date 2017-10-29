def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def rad(n):
    p=1
    if prime(n)==True:
        return n
    for i in range(1,n+1):
        if n%i==0:
            if prime(i)==True:
                p*=i
    
    return p
d={}
for n in range(1,100001):
    print(n,rad(n))
    d[n]=rad(n)
e=[0]+sorted(d,key=d.get)
print(e[10000])
        
        
