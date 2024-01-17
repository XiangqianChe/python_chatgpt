# Part 20: Best Practices and Advanced Tips in Python


# 1. Code Style and PEP 8

# Follow PEP 8 for code style conventions.
# PEP 8: https://www.python.org/dev/peps/pep-0008/

# Good example:
def add_numbers(a, b):
    result = a + b
    return result


# Bad example:
def addNumbers(a,b):
    result=a+b
    return result


# 2. Debugging Techniques

# Use the 'pdb' module for interactive debugging.
# Example:
import pdb


def divide(a, b):
    pdb.set_trace()
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Run the function and enter 'c' to continue with debugging.


# 3. Performance Optimization

# Use the 'timeit' module to measure code execution time.
# Example:
import timeit


def slow_function():
    import time
    time.sleep(2)


# Measure execution time
execution_time = timeit.timeit(slow_function, number=1)
print(f"Execution Time: {execution_time} seconds")

# Use appropriate data structures and algorithms for efficiency.

# 4. Advanced String Formatting

# f-strings (Python 3.6+)
name = "Alice"
age = 30
formatted_string = f"Hello, {name}! You are {age} years old."

# Old-style formatting
formatted_string_old = "Hello, %s! You are %d years old." % (name, age)

# 5. Context Managers

# Use 'with' statement for resource management.
# Example:
with open("example.txt", "r") as file:
    content = file.read()
    # Process the file content


# 6. Decorators

# Create and use decorators for code reuse and extensibility.
# Example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


# 7. Type Hints

# Use type hints for better code readability and editor support.
# Example:
def add_numbers(a: int, b: int) -> int:
    return a + b

# 8. Virtual Environments

# Use virtual environments to isolate project dependencies.
# Example:
# Create a virtual environment: python -m venv myenv
# Activate virtual environment: source myenv/bin/activate (Linux) or myenv\Scripts\activate (Windows)

# 9. Version Control

# Use version control systems (e.g., Git) to track changes in your code.

# 10. Documentation

# Write clear and concise documentation for your code using docstrings.
# Use tools like Sphinx for generating documentation.

# 11. Testing

# Write unit tests for your code using frameworks like 'unittest' or 'pytest'.
# Test-driven development (TDD) can be a good practice.

# 12. Continuous Integration (CI)

# Use CI tools (e.g., Travis CI, Jenkins) to automate testing and deployment processes.

# 13. Code Reviews

# Conduct and participate in code reviews to improve code quality.

# 14. Keep Learning

# Stay updated with the latest developments in Python.
# Attend conferences, read books, and participate in the Python community.

# 15. Security

# Be mindful of security best practices.
# Avoid hardcoded sensitive information, use secure libraries for encryption, and follow security guidelines.

# 16. Modularization

# Break down code into smaller, modular functions and classes.
# Promote code reusability and maintainability.

# 17. Use Built-in Functions and Libraries

# Leverage built-in functions and standard libraries to avoid reinventing the wheel.
# Python has a rich set of libraries for various tasks.

# 18. Contribute to Open Source

# Contribute to open source projects to gain experience and improve your skills.
# Collaborate with the Python community.

# 19. Stay Consistent

# Maintain consistency in coding style, project structure, and naming conventions.
# Make your code predictable and easy to understand.

# 20. Plan and Design

# Before coding, plan and design your solution.
# Understand the problem, break it down, and choose appropriate algorithms and data structures.

# End of Part 20
