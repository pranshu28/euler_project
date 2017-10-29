r=10**5
def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
p=[]
for i in range(2,r):
    if prime(i):
        p.append(i)
def check(nr):
    nr = sorted(str(nr))
    for i in range(1,len(nr)+1):
        if nr[i - 1] != str(i):
            return False
    return True    
for t in p:
    if t>10**4:
        if check(t):
            print (t)
        else:
            continue
        
