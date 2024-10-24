a=[1,2,3,4]
b=['a','b','c','d']

print(a)
c=map(lambda x,y:(x,y), a,b)
d=list(c)
print(d)

a=[1,2,3,4]
b=['a','b','c','d']

c=lambda x,y:(x,y)
e=map(c,b)
el=list(e)
d=list(c)
print(d)
print(d)