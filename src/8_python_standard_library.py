# Part 8: Python Standard Library

# 1. os Module
import os

# Get the current working directory
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# List files in the current directory
files_in_directory = os.listdir(current_directory)
print("Files in Current Directory:", files_in_directory)

# Create a new directory
new_directory = "new_directory"
os.mkdir(new_directory)
print(f"Created a new directory: {new_directory}")

# 2. sys Module
import sys

# Display command line arguments
print("Command Line Arguments:", sys.argv)

# Display Python version
print("Python Version:", sys.version)

# 3. math Module
import math

# Calculate square root
sqrt_result = math.sqrt(25)
print("Square Root of 25:", sqrt_result)

# Calculate factorial
factorial_result = math.factorial(5)
print("Factorial of 5:", factorial_result)

# 4. random Module
import random

# Generate a random integer
random_integer = random.randint(1, 10)
print("Random Integer between 1 and 10:", random_integer)

# Generate a random float
random_float = random.uniform(1.0, 5.0)
print("Random Float between 1.0 and 5.0:", random_float)

# Print Results
print("\nPython Standard Library Results:")
# Results are also printed in each block above.
