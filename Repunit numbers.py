from fractions import gcd
def r(k):
    ans=0
    for i in range(k+1):
        ans+=10**i
    return ans
def check(n):
    if gcd(n,10)!=1:
        return -1
    k=2
    while int(r(k))%n!=0:
        k+=1
    return(k+1)
t=input()
t=int(t)
inp=[]
outp=[]
for k in range(0,t):
    n=input()
    inp.append(int(n))
for i in inp:
    print(int(check(i)))