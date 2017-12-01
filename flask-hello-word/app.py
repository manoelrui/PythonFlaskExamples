# Flask Hello Worls

# Import the flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# Use decorator to link the function to url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which return a string
def hello_world():
	return "Hello, World"

if __name__ == "__main__":
	app.run()


