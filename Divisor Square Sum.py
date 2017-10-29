import timeit
start = timeit.default_timer()

def prime(n):
    for i in range(2,int(n*.5)+1):
        if n%i==0:
            return False
    return True
def sm(n):
    s=0
    for d in range(1,n+1):
        if n%d==0:
            s+=d**2
    return s
def sm1(n):
    s=1
    for p in range(2,int(n/2)+1):
        if prime(p):
            pi=p
            while n%pi==0:
                pi*=p
            t=1
            if pi==p*p:
                t=p*p+1
            elif pi>p*p:
                t=(pi*pi-1)/(p*p-1)
            s*=t
    return s
s=1
for n in range(1,64000000):
    x=sm(n)**.5
    if x-int(x)==0 and x!=1:
        print(n,n**.5,x)
        s+=n
print(s)

stop = timeit.default_timer()
print ("Time : ",stop - start )
