import numpy as np

### INDEXING & SLICING 1D ARRAY ###
x= np.arange(0,20)
print(x)

print("Access by element")
print(x[8])
print(x[-1])
print(x[:10])
print(x[10:])
print(x[2:5])
print(x[-10:-1])

print("Replacing value in index 5 to 14 to 40")
y=x[5:15]=40
print(y)
print(x)

print("Copy list x to y")
y=x.copy()
print(y)


### INDEXING & SLICING 2D ARRAY ###
x = np.arange(25).reshape(5,5)
print(x);
print("Access element at row=3, column=4")
print(x[3][4])
print(x[3,4])

print("Slicing 2,3,4,7,8,9")
print(x[0:2, 2:])
print("Slicing 6,7,8,11,12,13,16,17,18")
print(x[1:4,1:4])

print("Checking conditions")
y=np.arange(1,20)
print(y)
print("Whether element is > 12")
print(y>12)
print("Values where y > 12")
print(y[y>12])