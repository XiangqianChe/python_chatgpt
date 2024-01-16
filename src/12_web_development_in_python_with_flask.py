# Part 12: Web Development in Python with Flask

# Install Flask: pip install Flask

# 1. Basic Flask App
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! This is a basic Flask web app.'


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
