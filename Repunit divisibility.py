import timeit
start = timeit.default_timer()



def gcd5(a):  
    if a%5!=0:
        return True
    return False
def a(n):
    k=1
    x=1
    while (x!=0):
        x=(x*10+1)%n
        k+=1
    return k
n=1000001
while True:
    if gcd5(n)==True:
        print(n,a(n))
        if a(n)>1000000:
            break
    n+=2
print(n)


stop = timeit.default_timer()
print ("Time : ",stop - start )
        
    
   
