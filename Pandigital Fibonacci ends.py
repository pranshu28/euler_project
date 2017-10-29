def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
def check1(nr):
    nr = sorted(str(nr)[:9])
    for i in range(1,len(nr)+1):
        if nr[i-1] != str(i):
            return False
    return True
def check2(nr):
    nr = sorted(str(nr)[-9:])
    for i in range(1,len(nr)+1):
        if nr[i-1] != str(i):
            return False
    return True 
for i in range(329466,329470):
    print(i)
    if (fib(i)>10**21) and check1(fib(i))==True and check2(fib(i))==True:
        break
print(i,fib(i)%10**10)
        
