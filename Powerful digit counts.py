def check(n,i):
    n=str(n)
    if i==len(n):
        return True
    return False
k=0
r=1001
for j in range(1,r):
    for i in range(1,r):
        if check(j**i,i):
            k+=1
print(k)            
