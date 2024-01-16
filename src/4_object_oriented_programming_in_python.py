# Part 4: Object-Oriented Programming (OOP) in Python

# 1. Classes and Objects
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Create instances of the classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")


# 2. Inheritance and Polymorphism
class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# Create instances of the subclasses
my_square = Square(5)
my_circle = Circle(3)


# 3. Encapsulation and Abstraction
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # _balance is a convention indicating it's a protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self._balance


# Create an instance of the BankAccount class
my_account = BankAccount(1000)

# Accessing and modifying balance using encapsulation
my_account.deposit(500)
my_account.withdraw(200)

# Get the current balance using abstraction
current_balance = my_account.get_balance()

# Print Results
print("Classes and Objects Results:")
print(f"{my_dog.name} says: {my_dog.make_sound()}")
print(f"{my_cat.name} says: {my_cat.make_sound()}")

print("\nInheritance and Polymorphism Results:")
print(f"Area of Square: {my_square.area()}")
print(f"Area of Circle: {my_circle.area()}")

print("\nEncapsulation and Abstraction Results:")
print(f"Current Balance: ${current_balance}")
