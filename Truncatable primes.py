import timeit
start = timeit.default_timer()

def prime(n):
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            return False
    return True
def check(n):
    x=len(str(n))
    for i in range(1,x):
        if prime(int(n/10**i))==False or n%10==1:
            return False
    return True

i=101
s=186
while True:
    if (i%10==3 or i%10==7 or str(i)[0]==3 or str(i)[0]==7) and prime(i) and check(i) and check(int(str(i)[::-1])):
        s+=i
        print(i,s)
    i+=2
print(s)
stop = timeit.default_timer()
print ("Time : ",stop - start )
