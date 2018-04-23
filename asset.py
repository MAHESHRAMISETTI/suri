class assets(object):
	"""doc string for assets"""
	def __init__(self,name,price,quantity):
		self.name=name
		self.price=price
		self.quantity=quantity
	def details(self):
		print('there are',self.name,'of',self.price,'and in this much',self.quantity,'quantity')

c1=assets('chair',800,45)
c1.details()








