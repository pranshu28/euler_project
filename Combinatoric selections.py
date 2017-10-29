def fact(n):
    f=1
    if n==0:
        return 1
    for i in range(1,n+1):
        f*=i
    return f
ncr=1
k=0
for n in range(1,101):
    for r in range(n+1):
        ncr=fact(n)/(fact(r)*fact(n-r))
        if ncr>10**6:
            k+=1
print(k)            
