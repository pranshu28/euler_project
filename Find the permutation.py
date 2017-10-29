import itertools
def perm(n):
	return list(itertools.permutations(range(1,n+1)))
t=int(input())
for i in range(t):
	n,k=input().split(" ")
	n=int(n)
	k=int(k)
	per=perm(int(n))
	arr=[]
	ans=[]
	for i in per:
		dist=[]
		for x in range(n-1):
			dist.append(abs(i[x]-i[x+1]))
		arr.append(min(dist))
	for j in per:
		if arr[per.index(j)]==max(arr):
			ans.append(j)
	if len(ans)<k:
		print("-1")
	else:
		print(*ans[k-1])
	
