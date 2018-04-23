a=[[1,2],[4,3]]
b=[[4,5],[6,7]]
c=[[0,0],[0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		c[i][j]=a[i][j]+b[i][j]

for r in c:
  print(r)	







 for i in range(len(a)):
 	for j in range(len(a[0])):
 		c[i][j]+=(a[i][j]*b[i][j])+(a[i][j]*b[i][j])

 for r in c:
  print(r)	 		