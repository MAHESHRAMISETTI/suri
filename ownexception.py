class Error(Exception):
	'''This is the base class exception'''
	pass
class underageError(Error):
	'''This is raised when the input age is lessthan the determined age'''
	pass
class overageError(Error):
	'''This is called when the age of person is overthan the determined age'''
	pass
class NotyetBornError(Error):
	''' this is called when the person enter 0'''
	pass
age=25
while True:
	try:
		inputage =int(input('enter the age person'))
		if inputage <= 0:
			raise NotyetBornError
		elif inputage<age:
	  		raise underageError
		elif inputage>age:
			raise overageError
		break
	except NotyetBornError:
		print('the person is not yet born')
		print('try agian------!!!!')
	except underageError:
		print('the person age is less than what you think')
		print('try agian------!!!!')
	except overageError:
		print('the person age is more than what you think')
		print('try agian------!!!!')
	finally:
		print('you have entered some age-----')
print('you have guessed age correctly-----!!!!')