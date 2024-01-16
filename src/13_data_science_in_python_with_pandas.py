# Part 13: Data Science in Python with pandas

# Install pandas: pip install pandas

# 1. Basic pandas Operations
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Harry', 'Hermione', 'Ron', 'Ginny'],
        'Age': [22, 23, 21, 19],
        'House': ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Gryffindor']}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic DataFrame operations
print("\nBasic DataFrame Operations:")
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print("Info:")
df.info()

# Accessing data in DataFrame
print("\nAccessing Data:")
print("Name column:")
print(df['Name'])
print("\nRow with index 1:")
print(df.loc[1])
print("\nFilter by Age:")
print(df[df['Age'] > 21])

# 2. Reading and Writing Data
# Writing DataFrame to a CSV file
df.to_csv('students.csv', index=False)

# Reading data from a CSV file into a DataFrame
new_df = pd.read_csv('students.csv')

# Display the new DataFrame
print("\nNew DataFrame from CSV:")
print(new_df)
