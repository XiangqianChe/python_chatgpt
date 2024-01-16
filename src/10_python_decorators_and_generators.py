# Part 10: Python Decorators and Generators

# 1. Creating and Using Decorators
# Decorator to measure the execution time of a function
import time


def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time of {func.__name__}: {end_time - start_time:.4f} seconds")
        return result
    return wrapper


# Applying the decorator to a function
@measure_execution_time
def slow_function():
    time.sleep(2)
    print("Function executed.")


slow_function()


# 2. Understanding Generators and Iterators
# Generator function to generate Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Using the generator to print the first 5 Fibonacci numbers
fibonacci_sequence = fibonacci_generator(5)
print("Fibonacci Sequence:", list(fibonacci_sequence))

# Print Results
print("\nDecorators and Generators Results:")
# Execution time is also printed when calling slow_function.
