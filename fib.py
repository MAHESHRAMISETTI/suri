def fib(n):
 	a,b=0,1
 	while a<n:
 		print(a,end='')
 		a, b=b, a+b
 	print()
fib(10000)
 		

n=int(input('enter the no of rows'))
	for i in range(n,0,-1):
		print((n-i) * ' ' +i *  '*')














