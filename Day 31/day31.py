import numpy as np
# a = np.arange(15).reshape(3, 5)

# print(a.shape) #return tuple
# print(a.ndim)  #return row X column
# print(a.dtype.name) # prints data type eg. int64 float64
# print(a.itemsize) #bits it taking
# print(a.size) #total elements
# print(type(a)) #numpy.ndarray
# b = np.array([6, 7, 8])
# print(type(b)) #numpy.ndarray


# c = np.array([(1,0,3), (4,5,6)], dtype=bool) #creating an array 2D dtype is optional 
# print(c)

# d = np.empty((2, 3)) 
# print(d) 

# e = np.arange(1, 121).reshape(2,3,5,2,2) 
# print(e)


from numpy import pi
np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
f = np.sin(x)