#functions
def greet(name):
    return "Hello, " + name + "!"
print(greet("Alice"))
##multiple arguments
def add(a, b):
    return a + b
print(add(5, 3))


#finding factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))


#finding whether a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(11))

#factorial of a number
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
print(fibonacci(10))


#Reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello World"))


#count vowels in a string
def count_vowels(s):    
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
print(count_vowels("Hello World"))

#finding palindrome
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))


#convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(25))


#convert fahrenheit to celsius
def lcm(x, y):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    return x * y // gcd(x, y)
print(lcm(4, 5))


#sum of squares of n natural numbers
def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))
print(sum_of_squares(5))


#reverse a list
def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))



#decimal to binary
def decimal_to_binary(n):
    return bin(n).replace("0b", "")
print(decimal_to_binary(10))

#binary to decimal
def binary_to_decimal(b):
    return int(b, 2)
print(binary_to_decimal('1010'))


#greatest common divisor
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
print(gcd(48, 18))


#sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(12345))


#power of a number
def power(base, exp):
    return base ** exp
print(power(2, 3))




#Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}
print(merge_dicts({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))


#Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


#Sum of all elements in a list
def sum_of_list(lst):
    return sum(lst)
print(sum_of_list([1, 2, 3, 4, 5]))
print("Sum of list:", sum_of_list([1, 2, 3, 4, 5]))



#Count number of words in a string
def count_words(s):
    words = s.split()
    return len(words)
print(count_words("Hello world, this is a test string."))


#Calculate discounted price
def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)
print(calculate_discounted_price(100, 15))


#Calculate discounted price
def calculate_discounted_price(price, discount):
    return price - (price * discount / 100)
print(calculate_discounted_price(100, 15))


#MINI TASK
## Day 4
''' Take student name & marks

Calculate total

Calculate average

Return Pass / Fail

Print final resultt'''



def student(name,marks):
    total=sum(marks)
    average=total/len(marks)
    if average>=35:
        result = "pass"
    else:
        result ="fail"
    
    print("Name:",name)
    print("Total:",total)
    print("Average:",average)
    print("Result:",result)

#Taking Input
name=input("Name: ")
marks=[70,80,90]
student(name,marks)