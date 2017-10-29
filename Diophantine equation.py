def nat(x):
    if x>0 and x%1==0:
        return True
    else:
        return False
count=0
for n in range(1,10):
    for a in range(1,10**10):
        for b in range(1,a+1):
            if (nat((a**-1)+(b**-1))*(10**n)):
                count+=1
print("Total : ",count)                    
    
