def F(c,m,n):
    a,b = 0,1
    ans=[]
    i=0
    while i<2*n:
        a, b = b, a + b
        ans.append((c*c*(b*b+a*a))%m)
        i+=1
    print(len(set(ans[2:-1])))
i=[int(x) for x in input().split(" ")]
F(i[0],i[1],i[2])