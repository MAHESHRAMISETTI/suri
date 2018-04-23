Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=int(input('enter the value'))
enter the value5
>>> for a in range(1,11):
	print(num,'x',a,'=',num*a)

	
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
>>> 
>>> 
>>> a=5
>>> b=5
>>> print(a+b)
10
>>> a=[1,2,3,4,5,6,7,8,9,10]
>>> print(a(5))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(a(5))
TypeError: 'list' object is not callable
>>> print(a[5])
6
>>> print(type(a))
<class 'list'>
>>> print(count(a))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(count(a))
NameError: name 'count' is not defined
>>> print(sum(a))
55
>>> print(a[1:5])
[2, 3, 4, 5]
>>> print(a[::2])
[1, 3, 5, 7, 9]
>>> print(a[:])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(len(a))
10
>>> print(all(a))
True
>>> print(max(a))
10
>>> print(min(a))
1
>>> print(sorted(a))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 75/2
37.5
>>> 9&3
1
>>> 15&0
0
>>> 15/0
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    15/0
ZeroDivisionError: division by zero
>>> 0/5
0.0
>>> 5//3
1
>>> 5/3
1.6666666666666667
>>> t1=(1,2.3,3.4,5,4+5j,'hello')
>>> t2=('mahesh','suresh')
>>> print(t1+t2)
(1, 2.3, 3.4, 5, (4+5j), 'hello', 'mahesh', 'suresh')
>>> print(type(t1),type(t2))
<class 'tuple'> <class 'tuple'>
>>> print(t1(3))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(t1(3))
TypeError: 'tuple' object is not callable
>>> 	print(t1(3))
SyntaxError: unexpected indent
>>> print(t1[3])
5
>>> print(t1[3])
5
>>> table=[2*a for a in range(1,100)]
>>> 	print (table)
SyntaxError: unexpected indent
>>> print(table)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]
>>> a={1,2,3,4}
>>> b={5,3,6,1}
>>> print(a union b)
SyntaxError: invalid syntax
>>> print(a union(b))
SyntaxError: invalid syntax
>>> print(a-b)
{2, 4}
>>> print(b-a)
{5, 6}
>>> print(aub)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(aub)
NameError: name 'aub' is not defined
>>> print(a u b)
SyntaxError: invalid syntax
>>> print(a U b)
SyntaxError: invalid syntax
>>> print(a U b)
SyntaxError: invalid syntax
>>> print(a.union(b)))

