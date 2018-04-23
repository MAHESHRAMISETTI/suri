# while 1:
# 	a=int(input('enter a num in numerator'))
# 	b=int(input('enter a num  in denominator'))
# 	try:
# 		c=(a/b)
# 	except ZeroDivisionError:
# 		print('there is zero in denominator')
# 	else:
# 		print(c)
# 	finally:
# 		print('the code has been executed')




#raise
try:
	a=5
	print(a)
	raise NameError('hi bro!!!!!!')
except NameError as n:
	print('there is an exception')
	print(n)