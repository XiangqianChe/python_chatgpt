# Part 6: Functional Programming in Python

# 1. Higher-Order Functions
def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def apply_operation(func, number):
    return func(number)


result_square = apply_operation(square, 5)
result_cube = apply_operation(cube, 3)

# 2. Lambda Functions
power_of_four = lambda x: x ** 4

# 3. map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
cubed_numbers = list(map(cube, numbers))
power_of_four_numbers = list(map(power_of_four, numbers))

# 4. filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
positive_numbers = list(filter(lambda x: x > 0, numbers))

# 5. reduce function
from functools import reduce

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
product_of_numbers = reduce(lambda x, y: x * y, numbers)

# Print Results
print("Higher-Order Functions Results:")
print("Square of 5:", result_square)
print("Cube of 3:", result_cube)

print("\nLambda Functions Results:")
print("Power of Four of 2:", power_of_four(2))

print("\nmap Function Results:")
print("Squared Numbers:", squared_numbers)
print("Cubed Numbers:", cubed_numbers)
print("Power of Four Numbers:", power_of_four_numbers)

print("\nfilter Function Results:")
print("Even Numbers:", even_numbers)
print("Positive Numbers:", positive_numbers)

print("\nreduce Function Results:")
print("Sum of Numbers:", sum_of_numbers)
print("Product of Numbers:", product_of_numbers)
