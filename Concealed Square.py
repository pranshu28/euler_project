def check(x):
    i=1
    k=1
    print(x,x**2)
    while i<10:
        if (int(((x**2)%(10**(2*i+1)))/(10**(2*i))))!=(10-i):
            k=0
            break
        i+=1
    if k==1:
        print(x,"-\n-\n-\n-\n-\n-\n-\n\n\n\n\n\n\n--------")
        exit

x=int(1020304050697989900**.5)
y=int(1929394959697989900**.5)
l=[]
while y>x:
    if y%100==30 or y%100==70:
        for i in range(5,10):
            if (y**2)%(10**(2*i-1))>(11-i)*(10**(2*i-2)) and (y**2)%(10**(2*i-1))<(12-i)*(10**(2*i-2)):
                check(y)
                
    y-=1


    
        


    
        

