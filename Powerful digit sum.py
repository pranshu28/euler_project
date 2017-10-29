s=[]
def sum_digits(f):
    s=0
    c=str(f)
    for i in c:
        s+=int(i)
    return s
for i in range(100):
    for j in range(100):
        s.append(sum_digits(i**j))
x=max(s)
print("Max is ",x)        
    
