import numpy as np
b=np.ones(shape=(2,3,4))
b=np.random.randint(20,30,size=(5,2,3))
print(b)

print(b.ndim)
print(b.shape)
#np.transpose(b,(2,3,5))
r= b.transpose()
print(r)
print(r.shape)
r1=b.reshape(2,3,5)
print(r1)
print(b.max())
r4= np.empty((2,3,5))
print(r4)


