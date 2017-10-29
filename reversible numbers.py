import math
def rev(n):
    return int(str(n)[::-1])
def odd(s):
    k=1
    for i in str(s):
        if int(i)%2!=1:
            k=0
            break
    if k==1:
        return True
    else:
        return False
ans=0
def check(n):
    if ((n%10)%2==0 and (rev(n)%10)%2==1) or ((rev(n)%10)%2==0 and (n%10)%2==1):
        return True
    else:
        return False
for i in range(1,10**6):
    if odd(i+rev(i))==True and len(str(i))==len(str(rev(i))) and check(i)==True:
        print(i,rev(i),i+rev(i))
        ans+=1
    else:
        continue
print(ans)
    
