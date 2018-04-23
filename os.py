import os
while True:
	check = input("Want to shutdown your computer ? (y/n): ")
	if check == 'n':
		break
	else:
		os.system("shutdown /s /t 1")




# iterate through rows
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)		