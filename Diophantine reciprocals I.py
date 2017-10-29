def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
def fact(n):
    m=1
    for i in range(2,int(n/2)+1):
        if n%i==0:
            if prime(i):
                p=0
                while n%i==0:
                    n/=i
                    p+=1
            m*=(2*p+1)
    return m
n=180180
k=0
while True:
    c=0
    c=int((fact(n)/2))+1
    if c>k:
        k=c
        print(n,":",c)
    if c>4000000:
        break
    n+=1
                    













            
