# Part 7: File Handling in Python

# 1. Reading and Writing to Files
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("It contains multiple lines of text.\n")
    file.write("Feel free to add more lines!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("Content of the file:\n", content)

# 2. Working with CSV Files
import csv

# Writing to a CSV file
header = ["Name", "Age", "Country"]
data = [
    ("Harry", 22, "England"),
    ("Hermione", 23, "Scotland"),
    ("Ron", 21, "Wales")
]

with open("example.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header)
    csv_writer.writerows(data)

# Reading from a CSV file
with open("example.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print("CSV Row:", row)

# 3. Working with JSON Files
import json

# Writing to a JSON file
data_dict = {
    "name": "Harry Potter",
    "age": 22,
    "house": "Gryffindor"
}

with open("example.json", "w") as json_file:
    json.dump(data_dict, json_file, indent=2)

# Reading from a JSON file
with open("example.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("JSON Data:", loaded_data)

# Print Results
print("\nFile Handling Results:")
# Results are also printed in each block above.
