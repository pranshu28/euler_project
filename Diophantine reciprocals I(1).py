m=0
n=120120
while 1:
	c=0
	for i in range(1,n+1):
		if (n*n)%i==0:
			#print("--------",i,(n*n)%i,(n*(n+i))%i)
			c+=1
	if c>m:
		m=c
		print(n,m)
	if(m>=1000):
		break
	else:
		n+=20