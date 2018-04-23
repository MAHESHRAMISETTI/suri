Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=('mahesh')
>>> print(a)
mahesh
>>> l1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
NameError: name 'b' is not defined
>>>  L1=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
SyntaxError: unexpected indent
>>> L1=[1,2,3,4,5]
>>> print(len(L1))
5
>>> print(del(3))
SyntaxError: invalid syntax
>>> print(del(L3))
