def check(n):
    x=sorted(str(n))
    z=[]
    for i in str(n):
        z.append(i)
    if x==z or x[::-1]==z:
        return False
    return True
i=21780
c=19601
while True:
    if check(i)==True:
        c+=1
        print(i,c,c*100/i)
        if c*100/i==99:
            break
    i+=1
print(i,c,c*100/i)
