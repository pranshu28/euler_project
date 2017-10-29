import timeit
start = timeit.default_timer()
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
k=0
for x in range(1,578):
    if prime(3*x*x+3*x+1):
        k+=1
        print(x,3*x*x+3*x+1)    
    
print(k)

stop = timeit.default_timer()
print ("Time : ",stop - start )
