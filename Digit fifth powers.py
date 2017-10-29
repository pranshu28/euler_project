def check(n):
    m=str(n)
    s=0
    for i in m:
        s+=int(i)**5
    if s==n:
        return True
    return False
s=0
i=2
while i>1:
    if check(i):
        s+=i
        print(i,s)
    i+=1
print(s)
