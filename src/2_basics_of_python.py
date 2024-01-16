# Part 2: Basics of Python

# 1. Variables and Data Types
name = "Harry"
age = 11
height = 1.75
is_magical = True

# 2. Basic Operators
result_addition = age + 5
result_multiplication = age * 2
result_exponentiation = age ** 2
result_division = age / 2
result_remainder = age % 3

# 3. Control Flow: If Statements
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# 4. Control Flow: Loops
for i in range(3):
    print(f"Loop iteration {i}")


# 5. Functions
def greet_person(person_name):
    return f"Hello, {person_name}!"


greeting = greet_person(name)

# 6. Modules
# Assuming this code is in a file called basics_tutorial.py
# Create another file called helper_module.py with the following:
# def multiply_by_two(number):
#     return number * 2
# Then import and use it here:
from helper_module import multiply_by_two

result = multiply_by_two(age)

# Print results
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Magical:", is_magical)

print("\nBasic Operators Results:")
print("Addition:", result_addition)
print("Multiplication:", result_multiplication)
print("Exponentiation:", result_exponentiation)
print("Division:", result_division)
print("Remainder:", result_remainder)

print("\nControl Flow Results:")
print("Greeting:", greeting)

print("\nFunctions and Modules Results:")
print("Result after multiplying age by 2 using helper_module:", result)
