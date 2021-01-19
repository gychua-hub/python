import numpy as np
x = [[1,2,3],[4,5,6],[7,8,9]]

# display matrices
y = np.array(x)
print(y)

# Create 3x3 matrices with zeroes
print("Create 3x3 matrices with zeroes")
print(np.zeros((3,3)))

# Matrix operations
print("+5 to each element of the matrix that are initially 0s")
print(np.zeros((3,3)) + 5)
print("-5 to each element of the matrix that are initially 0s")
print(np.zeros((3,3)) - 5)
print("x5 to each element of the matrix that are initially 0s")
print(np.zeros((3,3)) * 5)
print("/5 to each element of the matrix that are initially 0s")
print(np.zeros((3,3)) / 5)
print("1X3 with element 1")
print(np.ones(3))
print("3x4 with element 1")
print(np.ones((3,4)))
print("4x4 with diagonal = 1")
print(np.eye(4))

print("Create matrix with range 10 (1D)")
print (np.arange(10))
print("Create matrix with range 20 (2D - 5x10)")
print(np.arange(50).reshape(5,10))

print("Linearly space")
print(np.linspace(0,1))
print(np.linspace(0,10,2))
print(np.linspace(0,100,5))

print ("max of [1,2,3,4,5] is: ")
x = [1,2,3,4,5]
y = np.array(x)
print (y.max())
print("At index")
print (y.argmax())
print ("min of [1,2,3,4,5] is: ")
print (y.min())
print("At index")
print (y.argmin())



print ("Random")
print(np.random.randn(5))
print(np.random.randint(1,100))