import timeit
start = timeit.default_timer()
t=0
i=4
def ch(n):
    if n**.5-int(n**.5)==0:
        return True
    return False
s=False
while s!=True:
    a=i*i
    j=3
    while j<i and s!=True:
        c=j*j
        f=a-c
        if ch(f)==True:
            if j%2==1:
                x=1
            else:
                x=2
            for k in range(x,j,2):
                d=k*k
                e=a-d
                b=c-e
                if ch(e)==True and b>0 and ch(b)==True:
                    print((d+c)/2,(e+f)/2,(c-d)/2)
                    s=True
                    break
        j+=1
    i+=1
print((d+c+e+f+c-d)/2)



stop = timeit.default_timer()
print ("Time : ",stop - start )
