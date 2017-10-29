import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
df = pd.read_csv("p107_network.txt", header=None)
df.as_matrix()
data=[]
for i in range(len(df)):
	row=[]
	for j in df[i]:
		if j!='-':
			row.append(int(j))
		else:
			row.append(0)
	data.append(row)
X=csr_matrix(data)
print(X)
Tcsr = minimum_spanning_tree(X)
ans=Tcsr.toarray().astype(int)
A=np.sum(np.array(data))
b=np.sum(np.array(ans))
print(A/2-b)