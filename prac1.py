#1
import numpy as np
array=np.arange(5,51,5)
print(array)
#2
array=np.array([np.arange(5,30,5),np.arange(30,51,5)])
print(array)
m=array.reshape(2,5)
print(m)
#3
print(array.shape)
print(array.ndim)
print(array.dtype)