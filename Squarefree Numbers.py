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
def check(n):
    for i in soe(int(n**.5)+1):
        if i>1 and n%i**2==0:
            return False
    return True
c=0
for i in range(1,2**20):
    if check(i):
        c+=1
print(c)

stop = timeit.default_timer()
print ("Time : ",stop - start )
