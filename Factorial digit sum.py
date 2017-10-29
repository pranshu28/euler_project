n=100
f=1
for i in range(1,101):
    f*=i
print(f)    
s=0    

c=str(f)
for i in c:
    s+=int(i)
print("sum is ",s) 
