from flask import Flask, render_template,request

## WSGI APP
app = Flask(__name__)

## Basic Routes

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'   
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)