a=10
def f1():
	a=23
	print(a)
def f2():
	a=45
	print(a)
a=67
print(a)	

f1()
f2()


num=int(input('enter the value'))
for a in range(1,21):
	print(num,'x',a,'=',num*a)


import time;

localtime = time.localtime(time.time())
print ("Local current time :", localtime)



localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


def fib(n):
	a,b=0,1
	while a<n:
		print(a,end='')
		a,b=b,a+b

print()
fib(1000)

n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')


a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])


n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()
























