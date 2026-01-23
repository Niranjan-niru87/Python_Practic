#Datasets in mechine learning
import pandas as pd

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 40, 50, 60, 65, 80]
}

df = pd.DataFrame(data)
print(df)

#Types of mechine learning
"Supervised ------> both inputs and outputs"
"Unsupervised  -------> only inputs No outputs"


#Train data and Test Data
"Train Data -----> which can train the Ml Model"
"Test Data -----> Which can test the Trained Data Model"


#Features(x) and Target(Y)
"Feature(X)  ------> input data"
"Target(Y) --------> Output data"


#Trained first model for mechine learning(Linear Regression)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [35, 40, 50, 60, 65, 80]
}

df = pd.DataFrame(data)

X = df[["Hours"]]   # Features
y = df["Marks"]     # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)


#Mini Task
'''MINI TASK (MANDATORY)

Train a model on this dataset:

Hours = [1,2,3,4,5,6,7]
Marks = [30,40,50,55,65,75,85]


Predict marks for Hours = 8

Print the prediction clearly like:

Predicted marks for 8 hours: __'''

from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset
Hours = [1, 2, 3, 4, 5, 6, 7]
Marks = [30, 40, 50, 55, 65, 75, 85]

# Convert to NumPy arrays and reshape
X = np.array(Hours).reshape(-1, 1)
y = np.array(Marks)

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict for 8 hours
prediction = model.predict([[8]])

print(f"Predicted marks for 8 hours: {prediction[0]:.2f}")
