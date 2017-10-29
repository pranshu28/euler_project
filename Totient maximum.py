from fractions import gcd
ans=[]
for n in range(2,1000):
    k=0
    for i in range(1,n):
        if gcd(n,i)==1:
            k+=1
    x=n/k
    print(n,k,x)
    ans.append(x)
print(max(ans),ans.index(max(ans))+2)
