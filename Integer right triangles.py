import math
def sqrt(n):
    if math.sqrt(n)%1==0:
        return True
    else:
        return False
r=1000

cnt=[]
def check(p):
    l=0
    for a in range(1,p):
        for b in range(1,p):
            if a>b and sqrt(a**2+b**2) and a+b+math.sqrt(a**2+b**2)==p:
                print(p,"-",a,b,math.sqrt(a**2+b**2))
                l+=1
    return l
for i in range(r+1):
    cnt.append(check(i))
print(max(cnt))
    
                    
    
    
