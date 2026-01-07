class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_result(self):
        total = sum(self.marks)
        average = total / len(self.marks)

        if average >= 35:
            result = "Pass"
        else:
            result = "Fail"

        print("Name:", self.name)
        print("Total:", total)
        print("Average:", average)
        print("Result:", result)


# Creating object
s1 = Student("Niru", [70, 80, 60, 90, 75])
s1.calculate_result()
s2 = Student("sniper", [70, 80, 60, 90, 0])
s2.calculate_result()



#oops concept
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Dog(Animal):
    def speak(self):
        return "Woof!"
    

class Cat(Animal):
    def speak(self):
        return "Meow!"



class Cow(Animal):
    def speak(self):
        return "Moo!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")
print(dog.name + " says " + dog.speak())
print(cat.name + " says " + cat.speak())
print(cow.name + " says " + cow.speak())



#class and object
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
car1 = Car("Toyota", "Camry", 2020)
car1.display_info()
car2 = Car("Honda", "Civic", 2019)
car2.display_info()



#opps concept inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, position):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
emp1 = Employee("Niru", 30, "E123", "Developer")
emp1.display_info()


#oops concept polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print("Area:", shape.area())


#oops concept encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print("Current Balance:", account.get_balance())



