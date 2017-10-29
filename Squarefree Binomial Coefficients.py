def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
def fact(n):
    if n==0:
        return 1
    f=n
    for i in range(1,n):
        f*=i
    return f
def nck(n,k):
    if k==0:
        return 1
    elif n==k:
        return 1
    
    ans=1
    for i in range(k+1,n+1):
        ans*=i
    return int(ans/fact(n-k))       
def sqf(n):
    for i in [4,9,25,49]:
        if n%i==0:
            return False
    return True
lst=[]
for n in range(51):
    for k in range(n+1):
        c=nck(n,k)
        if c not in lst:
            lst.append(c)
x=0
print(sum(lst))
for i in lst:
    if sqf(i)==False:
        x+=i
print(x,sum(lst)-x)
