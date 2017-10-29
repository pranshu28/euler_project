import math
def prime(n):
    k=0
    for i in range(2,n):
        if n%i==0:
            k=1
    if k==0:
        return True
    else:
        return False
p=[]
for i in range(2,7376508):
    if prime(i):
        p.append(i)
t=p[len(p)-1]
for i in p:
    for j in range(2,22,2):
        if i**j<t:
            p.append(i**j)
def uniq(p):
  output = []
  for x in p:
    if x not in output:
      output.append(x)
  return output
p=sorted(uniq(p))
i=1
for j in p:
    i*=j
    print(p.index(j)+1,j,i%500500507)
    if p.index(j)==500499:
        break
print("500500",j,i%500500507)
"""7376507"""
