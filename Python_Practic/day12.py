#zeroes()
def zeroes(n):
    import numpy as np
    arr = np.zeros(n)
    return arr
    return arr
print("Array of zeroes:", zeroes(5))


#ones()
def ones(n):
    import numpy as np
    arr = np.ones(n)
    return arr
    return arr
print("Array of ones:", ones(5))




#arange()
def create_arange_array(start, end, step):
    import numpy as np
    arr = np.arange(start, end, step)
    return arr
print("Array using arange from 0 to 10 with step 2:", create_arange_array(0, 10, 2))
print("Mean of all elements:", arr2d.mean())


#linspace()
def create_linspace_array(start, end, num):
    import numpy as np
    arr = np.linspace(start, end, num)
    return arr
print("Array using linspace from 0 to 1 with 5 elements:", create_linspace_array(0, 1, 5))

#full()
def create_full_array(shape, fill_value):
    import numpy as np
    arr = np.full(shape, fill_value)
    return arr

print("Array using full with shape (2,3) and fill value 7:", create_full_array((2, 3), 7))

#eye()
def create_eye_array(n):
    import numpy as np
    arr = np.eye(n)
    return arr
print("Identity matrix of size 4:", create_eye_array(4))

#random()
def create_random_array(shape):
    import numpy as np
    arr = np.random.random(shape)
    return arr
print("Random array with shape (2,3):", create_random_array((2, 3)))

#randint()
def create_randint_array(low, high, size):
    import numpy as np
    arr = np.random.randint(low, high, size)
    return arr
print("Random integer array between 1 and 10 with size 5:", create_randint_array(1, 10, 5))

#randn()
def create_randn_array(shape):
    import numpy as np
    arr = np.random.randn(*shape)
    return arr
print("Random normal array with shape (2,3):", create_randn_array((2, 3)))


#Boardcasting
import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([10, 20, 30])
broadcasted_array = array1 + array2
print("Broadcasted array:\n", broadcasted_array)

#Mini Task
'''Write a program that:

Creates a 3×3 random integer matrix (1 to 50)

Adds 5 to every element (broadcasting)

Prints:

Original matrix

Updated matrix

Max value

Min value

Mean value'''

import numpy as np

# Create a 3×3 random integer matrix (1 to 50)
matrix = np.random.randint(1, 51, size=(3, 3))

# Add 5 to every element (broadcasting)
updated_matrix = matrix + 5

# Print results
print("Original matrix:\n", matrix)
print("\nUpdated matrix (+5):\n", updated_matrix)

print("\nMax value:", updated_matrix.max())
print("Min value:", updated_matrix.min())
print("Mean:", updated_matrix.mean())


