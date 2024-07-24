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

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'   
    return render_template('form.html')

## Variable Rule

# @app.route("/success/<int:score>")
# def success(score):
#     return "The Marks you got is " + str(score)

@app.route("/success/<int:score>")
def success(score):
    res = " "
    if score >= 50:
        res = "PASSED"
    else: 
        res = "FAILED"
    
    return render_template('result.html', results=res)



if __name__ == "__main__":
    app.run(debug=True)