# Part 11: Concurrency and Parallelism in Python

# 1. Introduction to asyncio
import asyncio
import time


async def async_function(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"End {name}")


async def main_async():
    tasks = [async_function("Task 1"), async_function("Task 2"), async_function("Task 3"),
             async_function("Task 4"), async_function("Task 5"), async_function("Task 6"),
             async_function("Task 7"), async_function("Task 8"), async_function("Task 9")]
    await asyncio.gather(*tasks)


# Run the asyncio event loop
asyncio.run(main_async())


# 2. Basic Concepts of Multi-Threading
import threading


def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")


def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {letter}")


# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

# Print Results
print("\nConcurrency and Parallelism Results:")
# Results are also printed in each block above.
