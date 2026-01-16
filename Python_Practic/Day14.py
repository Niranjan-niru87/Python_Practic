#Pandas Data Cleaning (Missing Values + Filtering)
'''In real datasets, data is never perfect.
    Cleaning = 70% of ML work ✅'''

#Missing values (NaN)
import pandas as pd
import numpy as np
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David'],
    'Age': [25, np.nan, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame with Missing Values:\n", df)

#Handling Missing Values
#Filling missing values
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'City': 'Unknown'
})
print("\nDataFrame after Filling Missing Values:\n", df_filled)

#Filtering Data
filtered_df = df_filled[df_filled['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)

#isnull() / notnull()
print("\nRows with Missing Values:\n", df[df.isnull().any(axis=1)])
print("\nRows without Missing Values:\n", df[df.notnull().all(axis=1)])

#dropna() and fillna()
dropped_df = df.dropna()
print("\nDataFrame after Dropping Rows with Missing Values:\n", dropped_df)
filled_df = df.fillna('N/A')
print("\nDataFrame after Filling Missing Values with 'N/A':\n", filled_df)

#Filtering rows using conditions
age_above_30 = df_filled[df_filled['Age'] > 30]
print("\nRows where Age > 30:\n", age_above_30)
city_ny = df_filled[df_filled['City'] == 'New York']
print("\nRows where City is New York:\n", city_ny)

#multi-condition filtering
#AND condition
age_city_filter = df_filled[(df_filled['Age'] > 30) & (df_filled['City'] == 'Chicago')]
print("\nRows where Age > 30 and City is Chicago:\n", age_city_filter)
#OR condition
age_city_filter_or = df_filled[(df_filled['Age'] < 30) | (df_filled['City'] == 'Los Angeles')]
print("\nRows where Age < 30 or City is Los Angeles:\n", age_city_filter_or)

#Create Dataset with Missing Values (Practice)
import pandas as pd
import numpy as np

data = {
    "Name": ["Niru", "Ravi", "Sita", "Kiran"],
    "Age": [21, np.nan, 20, 23],
    "Marks": [70, 80, np.nan, 90]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())


#MINI TASK (MANDATORY)
'''Create a DataFrame with:

Name

Age (some missing)

City

Salary (some missing)

Then:

Print missing values count

Fill Age with mean

Fill Salary with mean

Filter employees with Salary > 30000'''

import pandas as pd
import numpy as np

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Niru", "Snipe", "Alex", "Ravi", "Meena"],
    "Age": [21, np.nan, 23, np.nan, 22],
    "City": ["Hyderabad", "Bangalore", "Chennai", "Delhi", "Mumbai"],
    "Salary": [35000, 28000, np.nan, 45000, np.nan]
})

print("Original DataFrame:\n", df)

# 1) Print missing values count
print("\nMissing values count:\n", df.isnull().sum())

# 2) Fill Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# 3) Fill Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nAfter filling missing values:\n", df)

# 4) Filter employees with Salary > 30000
filtered = df[df["Salary"] > 30000]
print("\nEmployees with Salary > 30000:\n", filtered)

