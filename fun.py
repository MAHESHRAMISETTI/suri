def welc(*a):
	for f in a:
		print('hi',f,'welcome to digital lync')
welc ('rahul','mahesh','vineet','suresh')


def details(**names):
	print(names)
	print(type(names))
	for name,roll in names.items():
		print('the roll number of ',name,'is',roll)
details (vineet=21,harshi=30,vikram=56,ironman=2)



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


a=10
def f1():
	global a
	a=23
	print(a)
def f2():
	a=45
	print(a)
a=67
print(a)	
f1()
f2()

b=(N**2 for N in range(0,5))
print(a)
for a in b:
	print(a)



























f1()
f2()



















