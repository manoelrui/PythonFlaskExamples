# Flask Hello Worls

# Import the flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

app.config["DEBUG"] = True

# Use decorator to link the function to url
@app.route("/")
@app.route("/hello")

# Define the view using a function, which return a string
def hello_world():
    return "Hello, World"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print value + 1
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print value + 1
    return "correct"

#dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print value
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()


