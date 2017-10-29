def sm(n,r):
    s=0
    for k in range(1,n+1):
        u=(900-3*k)*(r**(k-1))
        s+=u
    return s
n=5000
mx=-6*10**11
r=1
d=.1
while abs(sm(n,r)-mx)>1:
    if sm(n,r)>mx:
        r+=d
    else:
        r-=d
    print(r,sm(n,r))
    d/=2
print(r)
