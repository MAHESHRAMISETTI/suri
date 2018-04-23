class Private():
	def __init__(self):
		self.__update()
	def public(self):
		print('i am public member in private class')
	def update(self):
		print('i am the private member')
obj=private()
obj.public()	
obj.__update()