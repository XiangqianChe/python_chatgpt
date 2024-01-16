# Part 14: Machine Learning in Python with scikit-learn

# Install scikit-learn: pip install scikit-learn

# 1. Simple Machine Learning Task - Classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Generate a more meaningful dataset
# Features: [Study Hours, Sleep Hours]
X = [
    [5, 7],
    [3, 8],
    [8, 6],
    [2, 9],
    [7, 5],
    [4, 7],
    [6, 6],
    [3, 8],
    [5, 5],
    [7, 7]
]

# Labels: Pass ('P') or Fail ('F')
y = ['P', 'F', 'P', 'F', 'P', 'P', 'P', 'F', 'F', 'P']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create a k-nearest neighbors classifier
classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Print Results
print("Machine Learning Results:")
print("Predictions:", predictions)
print("Accuracy:", accuracy)
print("Classification Report:")
print(report)
