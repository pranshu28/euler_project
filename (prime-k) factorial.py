import timeit
start = timeit.default_timer()

def soe(n):
    pr=[]
    p=[0 for i in range(n)]
    for i in range(2,n):
        j=i*i
        while j<n:
            p[j-1]=1
            j+=i
    for k in range(1,n):
        if p[k-1]==0:
            pr.append(k)
    return pr
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
        f%=(n+5)
    return f
sm=0
r=10**3
for n in soe(r):
    if n>=5:
        x=(int(n/2)+fact(n-5)*(n-3))%n
        print(n,x)
        sm+=x
print(sm)
        

stop = timeit.default_timer()
print ("Time : ",stop - start )
