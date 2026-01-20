#What is Data Visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Line Plot (Trend Graph)
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Line Plot of Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
plt.bar(categories, values, color='skyblue')
plt.title("Bar Plot Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


#Create Dataset for Visualization
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 70000, 80000, 55000],
    "Department": ["HR", "Finance", "IT", "Marketing", "IT"]
}
df = pd.DataFrame(data)
print(df)

#Visualizing the Dataset
#Bar Plot of Age vs Name
plt.bar(df['Name'], df['Age'], color='purple')
plt.title("Age of Employees")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()

#Scatter Plot of Age vs Salary
plt.scatter(df['Age'], df['Salary'], color='red')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

#MINI TASK
#Create a DataFrame of students and marks and plot a bar chart


import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [70, 85, 60, 90]
}

df = pd.DataFrame(data)

plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
