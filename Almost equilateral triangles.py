r=10**9
p=r
c=0
s=0
for i in range(2,int(p/3)+1):
    k=0
    for j in [i-1,i+1]:
        p=2*i+j
        if p>10**9:
            k=1
        if ((p**.5)%10)%2==0:
            if ((4*i*i-j*j)**.5)%4==0 and p<r:
                print(i,i,j,p)
                s+=p
                c+=1
    if k==1:
        break
print(c,s)
