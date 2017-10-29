import timeit
start = timeit.default_timer()
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def ans(p,q):
    k=1
    while (k*(10**(len(str(p)))))%q!=q-p:
        k+=1
    return (k*(10**(len(str(p))))+p)
sm=0
x=999980
for p in range(5,x):
    if prime(p):
        q=p+1
        while q>p:
            if prime(q):
                y=ans(p,q)
                break
            q+=1
        print(p,q,y)
        sm+=(y)
print(sm)
stop = timeit.default_timer()
print ("Time : ",stop - start )



                    
                    
