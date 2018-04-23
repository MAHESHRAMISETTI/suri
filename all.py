# # # # # # a='HELLO'
# # # # # # # print(a[2])
# # # # # # # print(a[-3])
# # # # # # # print(a[-1])
# # # # # # # print(a[-1],a[-2],a[-3],a[-4],a[-5])
# # # # # # # print(a[ : ])
# # # # # # print(a[:4])

# # # # # # a='hi'
# # # # # # b='hello'
# # # # # # # print(a is b )
# # # # # # print('lo' in b)
# # # # # # print('lo' not in b)

# # # # # a='DigitalLync'
# # # # # print(len(a))
# # # # # print(a[5])
# # # # # print(a[0:7])
# # # # # print(a[::-2])
# # # # # print(a[::1])
# # # # # print(a.index('i'))
# # # # # print(type(a[8]))

# # # # a='MAHESH'
# # # # b='SURESH'
# # # # c='vineet'
# # # # print(a+b)
# # # # print(a,b)
# # # # print(a*5)

# # # a='MAHESH'
# # # b='SURESH'
# # # c='vineet'
# # # # print('{ } and { } are the classmates and { } is the teacher'.format(a,b,c))

# # # print('%s is friend of %s and %s is the boss of %s & %s % '(a,b,c))

# # # num=0
# # # if num>0:
# # # 	print('+ ve')
# # # elif num<0:
# # # 	print('- ve')
# # # elif num==0:
# # # 	print('zero num')

# # # for a in range (0,10,3):
# # # 	print(a)

# # # for num in range(0,100):
# # #  	print(num)

# # # a=20
# # # while a<25:
# # # 	a=a+1
# # # 	print(a)


# # # for a in 'mahesh':
# # # 	# if 'h'== 'a'
# # # 	# break
# # # 	print(a)


# # table=[2*a for a in range(1,100)]
# # print(table)




# # # a='mahesh'
# # # b=list(a)
# # # print(b)

# # l1=[1,2,3,5,8,7,9,4,6]
# # print(type(l1))
# # # print(len(l1))
# # # print(max(l1))
# # # print(min(l1))
# # # print(l1[2])
# # # print(4*l1)
# # # l1.append('mahesh')
# # # print(l1)

# # # l2=['mahi','suri','ram','krish']
# # # l1.extend(l2)
# # # print(l1)
# # # l1.insert(0,'i am the inserted element')
# # # print(l1)
# # # l1.remove(9)
# # # print(l1)
# # # print(l1.count( 1 ))

# # print(l1.reverse( ))

# names=('mahi','suri','ram')
# enum=enumerate(names)
# print(enum)
# for a in enum:
# 	print(a)

# names=('rahul','vineet','mahesh')
# for name in names:
# 	print('hi',name,'welcome to digital lync')



# # a=[num**2 for num in range(0,5)]
# # print(a)

# b=(n**2 for n in range(0,5))
# for a in b:
# 	print(b)

# a={a:a**2 for a in range (0,6)}
# print(a)


# # formkeys(seq,values)
# # key=[1,2,3,4,5]
# # v='hi'
# # print(type(v))
# # D1=Dict.formkeys(key,v)
# # print(D1)


# a={1,2,3,4,5}
# b=frozenset(a)
# print(type(b))
# print(b)

# sq2={'hello','ty','b','a','hello'}
# b=enumerate(sq2)
# print(type(b))
# for a in sq2:
# 	print(a)

def GM ( ):
	print('hello all good morning')
GM( )


def hello(a,b):
	print(a*b)
a=int(input('enter the value for a'))
b=int(input('enter the value for b'))
print('hello')
hello(a,b)


def add(a=6,b=3):
	print(a+b)
add()

def add(name,roll):
	print('the name of the student is ',name)
	print('the roll no of student is ',roll)
add(name='vineet',roll=3)



def add(table,chair,system,board):
	print('the pieces of table,chair,system,board is',table,chair,system,board)
add(table=1,chair=3,system=1,board=1)


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





































