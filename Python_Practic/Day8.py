#create of module in python
#PYTHON MODULE
#Creating Your Own Module
'''def add(a, b):
    return a + b

def sub(a, b):
    return a - b'''
#Using Your Module
'''import mymodule
result1 = mymodule.add(5, 3)
result2 = mymodule.sub(10, 4)
print(f"Addition: {result1}")
print(f"Subtraction: {result2}")'''

#Different Ways to Import a Module
#Import full module
'''import math
print(math.sqrt(16))
'''
#Import with alias
'''import math as m
print(m.sqrt(25))
'''
#Import specific functions
'''from math import sqrt, pow
print(sqrt(36))
'''
#PYTHON PACKAGE
#Example Modules Inside Package
'''def multiply(a, b):
    return a * b


def upper_text(text):
    return text.upper()

    
    
from my_package.math_ops import multiply
from my_package.string_ops import upper_text

print(multiply(3, 4))
print(upper_text("python"))
'''

#PIP (VERY IMPORTANT)
#Installing a Package
'''# Open your command prompt or terminal and run:
# pip install requests
'''
#Using an Installed Package
'''import requests
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
'''
#Check pip version
'''pip --version'''
#Install a package
'''pip install package_name'''
#Upgrade a package
'''pip install --upgrade package_name'''
#Uninstall a package
'''pip uninstall package_name'''
#pip list
'''pip list'''

#REAL-LIFE EXAMPLES (Jobs)
'''Task	Package
HTTP requests	requests
Data analysis	pandas
Web apps	flask, django
ML / AI	numpy, scikit-learn'''


#Mini task
import random

numbers = []

# Generate 5 random numbers
for i in range(5):
    num = random.randint(1, 100)
    numbers.append(num)

# Find max and min
maximum = max(numbers)
minimum = min(numbers)

print("Numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)


