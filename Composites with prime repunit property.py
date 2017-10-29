import timeit
start = timeit.default_timer()
def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
def r(k):
    s=''
    for i in range(k):
        s+=str(1)
    return int(s)
def gcd5(a):  
    if a%5!=0:
        return True
    return False
def a(n):
    k=1
    while True:
        if r(k)%n==0:
            break
        k+=1
    return k
k=1
s=0
n=91
while k<=25:
    if gcd5(n)==True and prime(n)==False and (10**(n-1))%(9*n)==1:
        print(k,n)
        k+=1
        s+=n
    n+=2
print(s)


stop = timeit.default_timer()
print ("Time : ",stop - start )
        
    
   
