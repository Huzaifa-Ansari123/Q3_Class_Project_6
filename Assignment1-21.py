# Assignment 1: Class Student with attributes name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Test the class
student = Student("John Doe", 90)
student.display()

# Assignment 2: Class Counter with class variable and class method
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")

# Test the class
counter1 = Counter()
counter2 = Counter()
Counter.display_count()

# Assignment 3: Class Car with public variable and public method
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("The car is starting.")

# Test the class
car = Car("Toyota")
print(car.brand)
car.start()

# Assignment 4: Class Bank with class variable and class method
class Bank:
    bank_name = "Bank of America"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def __init__(self):
        pass

# Test the class
bank1 = Bank()
print(bank1.bank_name)
Bank.change_bank_name("Wells Fargo")
bank2 = Bank()
print(bank2.bank_name)

# Assignment 5: Class MathUtils with static method
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Test the class
print(MathUtils.add(5, 10))

# Assignment 6: Class Logger with constructor and destructor
class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")

# Test the class
logger = Logger()
del logger

# Assignment 7: Class Employee with public, protected, and private variables
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")

# Test the class
employee = Employee("John Doe", 50000, "123-45-678")
print(employee.name)
print(employee._salary)
try:
    print(employee.__ssn)
except AttributeError:
    print("Error: cannot access private variable __ssn")
employee.display_details()

# Assignment 8: Class Person and Teacher with inheritance and super()
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display_details(self):
        print(f"Name: {self.name}, Subject: {self.subject}")

# Test the class
teacher = Teacher("John Doe", "Math")
teacher.display_details()

# Assignment 9: Abstract class Shape and Rectangle
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Test the class
rectangle = Rectangle(5, 10)
print(rectangle.area())

# Assignment 10: Class Dog with instance variables and instance method
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")

# Test the class
dog = Dog("Buddy", "Golden Retriever")
dog.bark()

# Assignment 11: Class Book with class variable and class method
class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_book_count(cls):
        print(f"Total books: {cls.total_books}")

# Test the class
book1 = Book()
book2 = Book()
Book.display_book_count()

# Assignment 12: Class TemperatureConverter with static method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Test the class
print(TemperatureConverter.celsius_to_fahrenheit(30))

# Assignment 13: Composition with classes Engine and Car
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("The engine is starting.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start_car(self):
        self.engine.start()

# Test the class
engine = Engine(200)
car = Car("Toyota", engine)
car.start_car()

# Assignment 14: Aggregation with classes Department and Employee
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Test the class
department = Department("Sales")
employee1 = Employee("John Doe")
employee2 = Employee("Jane Doe")
department.add_employee(employee1)
department.add_employee(employee2)
print(department.employees[0].name)

# Assignment 15: Method Resolution Order (MRO) and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

# Test the class
d = D()
d.show()

# Assignment 16: Function Decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called.")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test the decorator
say_hello("John Doe")

# Assignment 17: Class Decorator
def add_greeting(cls):
    class Wrapper(cls):
        def greet(self):
            return "Hello from Decorator!"
    return Wrapper

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorator
person = Person("John Doe")
print(person.greet())

# Assignment 18: Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

# Test the property decorators
product = Product(100)
print(product.price)
product.price = 200
print(product.price)
del product.price
try:
    print(product.price)
except AttributeError:
    print("Error: price attribute has been deleted.")

# Assignment 19: Callable and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Test the callable
multiplier = Multiplier(5)
print(multiplier(10))
print(callable(multiplier))

# Assignment 20: Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)

# Assignment 21: Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Test the iterable
for i in Countdown(5):
    print(i)
