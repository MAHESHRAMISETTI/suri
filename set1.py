a='hello'
b=set(a)
print(b)

b.pop( )
print(b)


A={1,2,3,4,5,6,7,8,9}
B={5,3,6,10}
print(A.union(B))
print(A.difference(B))
print(B.difference(A))


sq2={143.143,42,52,62,72}
print(len(sq2))



sq2={'hello','ty','b','a','hello'}
c=frozenset(sq2)
print(type(c))
print(c)

c.add(5)
print(c)

