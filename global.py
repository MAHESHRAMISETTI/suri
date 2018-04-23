a=10
>>> def f1():
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
