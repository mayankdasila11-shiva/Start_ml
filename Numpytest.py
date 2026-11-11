import numpy as np
import time as t
array=np.arange(1000000)  #This is an array
num=list(range(1000000))
# print(array)
# print(num)
#array consumes much less space then list.
t0=t.time()
sum(num)
print(f"list: {t.time()-t0}")
t1=t.time()
array.sum()
print(f"numpy: {t.time()-t1}")
ar1=np.ones((2,3))
print(ar1[0][0])
print(np.linspace(0,1,5))