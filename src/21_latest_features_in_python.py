# Part 21: Latest Features in Python

# 1. f-strings (Python 3.6+)

name = "Harry"
age = 17
formatted_string = f"Hello, {name}! You are {age} years old."


# 2. Type Hints (Python 3.5+)

def greet(name: str) -> str:
    return f"Hello, {name}!"


# 3. Async/Await (Python 3.5+)

import asyncio


async def async_greet(name: str) -> str:
    await asyncio.sleep(1)
    return f"Hello, {name}!"

# 4. Enumerate (Python 3.4+)

characters = ["Harry", "Ron", "Hermione"]

for index, character in enumerate(characters, start=1):
    print(f"Character {index}: {character}")

# 5. Pathlib (Python 3.4+)

from pathlib import Path

file_path = Path("example.txt")
content = file_path.read_text()
file_path.write_text("New content")

# 6. Data Classes (Python 3.7+)

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


# Creating instances of the Point class
point1 = Point(1.0, 2.5)
point2 = Point(x=3.0, y=4.5)

# Accessing attributes
print(point1.x, point1.y)  # Output: 1.0 2.5

# Automatic __repr__ method
print(point2)  # Output: Point(x=3.0, y=4.5)


# 7. Underscore in Numeric Literals (Python 3.6+)

number = 1_000_000
binary_number = 0b_0010_1010

# 8. Walrus Operator (Python 3.8+)

while (input_value := input("Enter a value: ")) != "exit":
    print(f"You entered: {input_value}")

# 9. Pattern Matching (Python 3.10+)

match_value = 2

match match_value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")
    case _:
        print("Value is something else")

# 10. Zoneinfo (Python 3.9+)

from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(ZoneInfo("America/New_York"))
print(f"Current time in New York: {now}")

# 11. Performance Improvements

# Each new Python version brings performance improvements. Upgrade to the latest version for optimized execution.

# Note: Always check the Python documentation for the most accurate and up-to-date information on the latest features.

# End of Part 21
