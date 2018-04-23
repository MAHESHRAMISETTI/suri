a=lambda a:a**2
print(a(45))


l=[a for a in range(0,5)]
print(l)



l2=list(map(lambda a:a%2==0,l))
print(l2)


l3=list(filter(lambda a:a%2!=0,l))
print(l3)

#import calendar
print(dir(calendar))
print(calendar. leap (2016))







