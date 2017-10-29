import timeit
start = timeit.default_timer()


def prime(n):
    k=0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False

def sm(n,r):
    s=0
    for p in range(2,n):
        if prime(p):
            pi=p
            while pi<=n:
                s+=p*(int(n/pi)-int(r/pi)-int((n-r)/pi))
                pi*=p
    return s
print(sm(200,15))       

stop = timeit.default_timer()
print ("Time : ",stop - start )
        
