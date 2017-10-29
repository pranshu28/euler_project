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

n=100000
p=soe(n)[1:]
c=1
for i in range(1,n+1):
    k=0
    for j in range(2,i+1):
        if i%j==0 and j in p:
            if j>5:
                k=1
                break
    if k!=1:
        print(i,c)
        c+=1

print(c)


stop = timeit.default_timer()
print ("Time : ",stop - start )
