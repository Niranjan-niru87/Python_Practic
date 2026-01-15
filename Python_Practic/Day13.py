#WHAT IS PADDAS
#Pandas is an open-source library that provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. It is built on top of another library called NumPy, which provides support for large, multi-dimensional arrays and matrices.
#Pandas is particularly well-suited for working with structured data, such as tabular data in spreadsheets or databases. It provides two primary data structures: Series (1-dimensional) and DataFrame (2-dimensional), which allow for efficient data manipulation, cleaning, and analysis.
#Pandas offers a wide range of functionalities, including data filtering, aggregation, merging, resh
# aping, and time series analysis. It also provides tools for handling missing data, data visualization, and input/output operations with various file formats (e.g., CSV, Excel, SQL databases).
    


#Series
import pandas as pd
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Pandas Series:\n", series)

#DataFrame
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("Pandas DataFrame:\n", df)

#DataFrame Operations
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)


#head() and tail()
print("First 2 rows of DataFrame:\n", df.head(2))
print("Last 2 rows of DataFrame:\n", df.tail(2))


#info() and describe()
print("DataFrame Info:")
df.info()
print("DataFrame Description:\n", df.describe())

#Quick Demo Program (All Functions)
import pandas as pd

df = pd.DataFrame({
    "Name": ["Niru", "Snipe", "Alex", "Ravi"],
    "Marks": [85, 90, 72, 40],
    "Passed": [True, True, True, False]
})

print("HEAD:\n", df.head())
print("\nTAIL:\n", df.tail())

print("\nINFO:")
df.info()

print("\nDESCRIBE:\n", df.describe())


#MINI TASK (MANDATORY)

'''Create a DataFrame with:

Name

Age

City

Then print:

First 2 rows

Column names

Average age'''

import pandas as pd

data = {
    "Name": ["Niru", "Ravi", "Sita", "Kiran"],
    "Age": [21, 22, 20, 23],
    "City": ["Gooty", "Anantapur", "Gooty", "Kadapa"]
}

df = pd.DataFrame(data)

print("First 2 rows:")
print(df.head(2))

print("\nColumns:")
print(df.columns)

print("\nAverage Age:")
print(df["Age"].mean())

