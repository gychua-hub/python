import numpy as np

### 1D array ###
x = np.arange(10)
print (x)
y = np.arange(10,20)
print (y)
print("addition of 2 lists")
z = x+y
print (z)
print("subtraction of 2 lists")
z = x-y
print (z)
print("multiplication of 2 lists")
z = x*y
print (z)
print("division of 2 lists")
z = x/y
print (z)
print("SINE of x")
print (np.sin(x))
print("LOG of x")
print (np.log(x))
print("max of x")
print (np.max(x))
print(x.max())
print ("sum of all elements in x")
print(x.sum())

### 2D array ###
x = np.arange(12).reshape(3,4)
print (x)
y = np.arange(10,22).reshape(3,4)
print (y)
print("addition of 2 lists")
z = x+y
print (z)
print("subtraction of 2 lists")
z = x-y
print (z)
print("multiplication of 2 lists")
z = x*y
print (z)
print("division of 2 lists")
z = x/y
print (z)
print("SINE of x")
print (np.sin(x))
print("LOG of x")
print (np.log(x))
print("max of x")
print (np.max(x))
print(x.max())
print ("sum of all elements in x")
print(x.sum())