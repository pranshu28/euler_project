import math
def check(n):
    x=str(n)
    s=0
    for i in x:
        s+=int(i)
    return s
c=0
k=[]
"""248155780267521"""
for i in range(8,100):
    for j in range(2,20):
        if check(i**j)==i:
            k.append(i**j)
k=sorted(k)
print(k)
            
       
