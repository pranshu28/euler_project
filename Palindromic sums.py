import math
def pal(n):
    n=str(n)
    if n==n[::-1]:
        return 1;
    else:
        return 0;
def check(l,d):
    sum=0
    for a in range(1,int(math.pow(l,.5))):
       n=2
       ans=0
       while ans<=l:
           ans=n*(a*a+(n-1)*(2*n-1)*d*d/6+(n-1)*a*d)
           if ans-int(ans)>.9999999:
               ans=int(ans)+1
           elif ans-int(ans)<.00000001:
               ans=int(ans)
           if pal(ans):
               sum+=ans
           n+=1
    return sum
t=input()
t=int(t)
inp=[]
for k in range(0,t):
    l,d=input().split()
    inp.append([int(l),int(d)])
for i in inp:
    print(int(check(i[0],i[1])))
        