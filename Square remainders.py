s=0
for a in range(3,1001):
	n=int((a-1)/2)
	r=2*n*a
	print(a,n,r,a*a)
	s+=r
print(s)