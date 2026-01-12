'''#Numpy in python
import numpy as np

#Creating array
arr1 = np.array([1,2,3,4,5])
print("Array 1:", arr1)
arr2 = np.array([[1,2,3],[4,5,6]])
print("Array 2:\n", arr2)
#Array attributes
print("Shape of arr2:", arr2.shape)
print("Data type of arr1:", arr1.dtype)
print("Size of arr2:", arr2.size)
#Array operations
arr3 = arr1 + 10
print("Array 1 after adding 10:", arr3)
arr4 = arr1 * 2
print("Array 1 after multiplying by 2:", arr4)
arr5 = arr1 + arr4
print("Array 1 + Array 4:", arr5)


#NumPy Array (fast & clean)
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a - b)
print(a / b)
print(a ** 2)

#Creating an ndarray
import numpy as np

arr = np.array([10, 20, 30])
print(arr)
print(type(arr))

#Creating a 2D array
import numpy as np
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
print("Shape of 2D array:", arr_2d.shape)
print("Data type of 2D array:", arr_2d.dtype)
print("Size of 2D array:", arr_2d.size)

#Import NumPy
import numpy as np


#Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#First NumPy Program
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Type:", type(arr))'''

#MINI task
import numpy as np

np_array = np.array([1,2,3,4,5,6,7,8,9,10])
print("Array: ", np_array)
print("Sum: ", np.sum(np_array))
print("Mean: ", np.mean(np_array))
print("Max: ", np.max(np_array))
print("Min: ", np.min(np_array))
