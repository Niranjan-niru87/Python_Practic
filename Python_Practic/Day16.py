#Scatter plot
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
marks = [35, 40, 50, 60, 65, 80]

plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

#histogram plot
import matplotlib.pyplot as plt
ages = [22, 25, 30, 35, 40, 28, 32, 26, 29, 31, 27, 34, 33, 38, 24]
plt.hist(ages, bins=5, color='green', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

#box plot
import matplotlib.pyplot as plt
data = [22, 25, 30, 35, 40, 28, 32, 26, 29, 31, 27, 34, 33, 38, 24]
plt.boxplot(data)
plt.title("Box Plot of Ages")
plt.ylabel("Age")
plt.show()

#Line plot
import numpy as np
x = np.linspace(0, 5, 100)
y = np.exp(x)
plt.plot(x, y)
plt.title("Exponential Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


#Mini Task Solution
'''Create a dataset of student marks and:

Plot a histogram

Plot a boxplot

Plot scatter between study hours and marks'''

import matplotlib.pyplot as plt

# Dataset
hours = [1,2,3,4,5,6,7]
marks = [30,40,50,55,65,75,85]

# 1) Histogram of marks
plt.hist(hours, bins=6)
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 2) Boxplot of marks
plt.boxplot(marks)
plt.title("Boxplot of Student Marks")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# 3) Scatter plot: study hours vs marks
plt.scatter(hours,marks)
plt.title("Study Hours vs Marks (Scatter Plot)")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
