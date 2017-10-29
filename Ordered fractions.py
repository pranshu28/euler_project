from fractions import Fraction
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

d=1000000
r=0
s=1
x=2
while d>x:
    n=(3*d-1)/7
    print(d,n)
    if s*n>r*d:
        s=d
        r=n
        x=(s/(3*s-7*r))
    d-=1
print(r,s)
            
    
            
            
