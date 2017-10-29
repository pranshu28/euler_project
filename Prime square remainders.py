def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
i=237203
c=21000
while True:
    i+=1
    if prime(i):
        if c%2!=0:
            r=2*c*i%i**2
            print(c,i,r)
            if r>10**10:
                break
        c+=1
print(c,i)
