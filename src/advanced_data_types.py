# Part 3: Advanced Data Types

# 1. Lists
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
fruits.extend(['watermelon', 'kiwi'])
fruits.insert(2, 'pear')
fruits.remove('banana')
last_fruit = fruits.pop()

# 2. Tuples
coordinates = (3, 4)
x, y = coordinates

# 3. Sets
unique_numbers = {1, 2, 3, 3, 4, 5}

# 4. Dictionaries
person = {'name': 'Hermione', 'age': 13, 'house': 'Gryffindor'}
person['role'] = 'student'
del person['age']

# 5. List Comprehensions
squared_numbers = [x**2 for x in range(5)]
even_numbers = [x for x in range(10) if x % 2 == 0]

# 6. String and String Formatting
movie = 'Harry Potter and the Philosopher\'s Stone'
book = 'Harry Potter {}'
formatted_book = book.format('and the Chamber of Secrets')
f_string = f"The movie is '{movie}' and the book is '{formatted_book}'"

# Print Results
print("Lists Results:")
print("Fruits:", fruits)
print("Last Fruit Removed:", last_fruit)

print("\nTuples Results:")
print("Coordinates:", coordinates)
print("Unpacked Coordinates (x, y):", x, y)

print("\nSets Results:")
print("Unique Numbers:", unique_numbers)

print("\nDictionaries Results:")
print("Person Dictionary:", person)

print("\nList Comprehensions Results:")
print("Squared Numbers:", squared_numbers)
print("Even Numbers:", even_numbers)

print("\nString and String Formatting Results:")
print("Formatted Book:", formatted_book)
print("F-String:", f_string)
