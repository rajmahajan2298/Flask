from flask import Flask

## WSGI APP
app = Flask(__name__)

## Basic Routes

@app.route("/")
def welcome():
    return "Welcome to our page"

@app.route("/index")
def index():
    return "Welcome to Index Page"

if __name__ == "__main__":
    app.run(debug=True)