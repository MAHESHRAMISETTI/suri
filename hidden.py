class cont:
	a =1
	__b = 2

	def inc(self,valu):
		self.__b += valu
		print(self.__b)


obj1 = cont()
obj1.inc(3)
# print(obj1.a)
# print(obj1.__b)
# print(obj1.__b)

# print(obj1._cont__b)
