# Part 5: Exception Handling in Python

# 1. Handling Exceptions with try, except, else, and finally
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"The result of {a} divided by {b} is: {result}")
    finally:
        print("This block always executes.")


# Test the divide_numbers function
divide_numbers(10, 2)
divide_numbers(5, 0)


# 2. Creating Custom Exceptions
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative."):
        self.message = message
        super().__init__(self.message)


def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    else:
        return number ** 0.5


# Test the calculate_square_root function
try:
    result_positive = calculate_square_root(25)
    print(f"The square root is: {result_positive}")
except NegativeNumberError as e:
    print(f"Error: {e}")

try:
    result_negative = calculate_square_root(-9)
    print(f"The square root is: {result_negative}")
except NegativeNumberError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes.")

# Print Results
print("\nException Handling Results:")
# Results are also printed in each block above.
