import decimal
def irr(n):
    n=str(n)
    if len(n)>100:
        return True
    return False
def no(a):
    n=decimal.Decimal(a)
    ans=decimal.Context(prec=105)
    return n.sqrt(ans)
def sum(n):
    s=0
    n=str(n)[:101]
    
    for i in n:
        if i=='.':
            continue
        else:
            s+=int(i)
    return s
print(no(2),sum(no(2)))
ans=0
for i in range(1,101):
    if irr(no(i))==True:
        print(sum(no(i)))
        ans+=sum(no(i))
print(ans)
