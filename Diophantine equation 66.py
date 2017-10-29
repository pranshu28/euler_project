def sqr(n):
    if (n**.5)%1==0:
        return True
    return False
l=[]
for d in range(2,1001):
    if sqr(d)==False:
        y=1
        while True:
            x=1+d*y*y
            if sqr(x)==True:
                print(x**.5,"^2 -",d,"*",y,"^2 = 1")
                l.append(int(x**.5))
                l.append(d)
                break
            y+=1
print(l[l.index(max(l))+1])
