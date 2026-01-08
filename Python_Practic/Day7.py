#Exception handling in Python
try:
    # Code that may raise an exception
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
# The finally block will always execute, regardless of whether an exception occurred or not.

# Custom Exception
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print(f"{number} is a positive number.")
try:
    num = int(input("Enter a positive number: "))
    check_positive(num)
except NegativeNumberError as nne:
    print(f"Error: {nne}")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")

# Using else block with try-except
try:
    num = int(input("Enter a number to check if it's even or odd: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
else:
    print("Input was processed successfully.")
finally:
    print("Execution completed.")


# Nested try-except
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
finally:
    print("Execution completed.")


#Mini task
try:
    total = int(input("Enter total marks: "))
    subjects = int(input("Enter number of subjects: "))
    average = total / subjects
except ZeroDivisionError:
    print("Error: Number of subjects cannot be zero")
except ValueError:
    print("Error: Please enter valid integers")
else:
    print("Average:", average)
finally:
    print("Calculation completed")
