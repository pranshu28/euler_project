a=[int(x) for x in input().split(" ")]
l1=[a[0],a[1],a[2],a[3]]
l2=[a[0],a[1],a[5]]
l3=[a[0],a[3],a[4]]
ans=min(sum(l1),sum(l2),sum(l3))
if ans>0:
	print(-1)
elif ans==0:
	print(0)
else:
	print(-1*ans)