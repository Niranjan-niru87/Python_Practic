#Indexing in 1D & 2D arrays
import numpy as np
#1D array indexing
arr1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1d)
print("Element at index 2:", arr1d[2])
#2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2d)
print("Element at row 1, column 2:", arr2d[1, 2])

#Array Slicing in 1D & 2D arrays
import numpy as np
#1D array slicing
arr1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1d)
print("Slice from index 1 to 4:", arr1d[1:4])
#2D array slicing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr2d)
print("Slice of rows 0-1 and columns 1-2:\n", arr2d[0:2, 1:3])

print("Original NumPy array:", np_array)
sliced_array = np_array[2:8]

#Slicing
print("Sliced array (index 2 to 7):", sliced_array)
#Advanced Slicing
advanced_sliced_array = np_array[[1, 3, 5, 7, 9]]
print("Advanced sliced array (indices 1,3,5,7,9):", advanced_sliced_array)
#Array Attributes & Operations
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print("Array 1:\n", arr1)

#Reshaping arrays
reshaped_array = np_array.reshape(2, 5)
print("Reshaped array (2x5):\n", reshaped_array)
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
print("Reshaped array (2x5):\n", reshaped_array)
print("Shape of reshaped array:", reshaped_array.shape)
print("Data type of reshaped array:", reshaped_array.dtype)


#MINI TASK
'''1.Creates an array from 1 to 12 
2.Reshapes it into 3 rows and 4 columns 
3.Prints: First row Last column 
4.Sum of all elements 
5.Mean of all elements'''

import numpy as np

# 1) Create array from 1 to 12
arr = np.arange(1, 13)

# 2) Reshape into 3 rows and 4 columns
arr2d = arr.reshape(3, 4)

print("Array (3x4):\n", arr2d)

# 3) First row
print("\nFirst row:", arr2d[0, :])

# 4) Last column
print("Last column:", arr2d[:, -1])

# 5) Sum of all elements
print("Sum of all elements:", arr2d.sum())

# 6) Mean of all elements
print("Mean of all elements:", arr2d.mean())
