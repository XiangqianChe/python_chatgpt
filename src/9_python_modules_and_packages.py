# Part 9: Python Modules and Packages

# 1. Creating and Using Modules
# Create a module named "my_module.py" with the following content:
# def greet(name):
#     return f"Hello, {name}!"

# In the main script:
import my_module

name_to_greet = "Harry"
greeting_result = my_module.greet(name_to_greet)
print("Greeting Result:", greeting_result)

# 2. Introduction to Packages
# Create a package named "my_package" with the following structure:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# In module1.py:
# def multiply(x, y):
#     return x * y

# In module2.py:
# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero!"

# In __init__.py (empty file or can contain package-level initialization code):
# from .module1 import multiply
# from .module2 import divide

# In the main script:
from my_package import multiply, divide

result_multiply = multiply(3, 4)
result_divide = divide(10, 0)

# Print Results
print("\nModules and Packages Results:")
print("Greeting Result from my_module:", greeting_result)
print("Result of Multiplication from my_package:", result_multiply)
print("Result of Division from my_package:", result_divide)
