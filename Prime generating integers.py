import timeit
start = timeit.default_timer()

def prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
def find(n):
    for d in range(1,int(n*.5)+1):
        if prime(d) and n%d==0:
            if prime(d+int(n/d))==False:
                return False
    return True
r=10**5
s=3
m=2
for n in range(6,r+1,2):
    if find(n) and prime(n+1) and ((n+1)%4==2 or (n+1)%4==3):
        s+=n
print("...",s)

stop = timeit.default_timer()
print ("Time : ",stop - start )
