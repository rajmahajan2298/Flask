from flask import Flask, render_template,request,redirect,url_for

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

## Jinja2 For 

@app.route("/successres/<int:score>")
def successres(score):
    res = " "
    if score >= 50:
        res = "PASSED"
    else: 
        res = "FAILED"
    
    exp = {'score': score, "res": res}
    
    return render_template('results1.html', results=exp)

## Jinja IF

@app.route("/successif/<int:score>")
def successif(score):
    
    return render_template('result.html', results=score)

## Fail 

@app.route("/fail/<int:score>")
def fail(score):
    
    return render_template('result.html', results=score)

@app.route("/submitone", methods=['POST', 'GET'])
def submitone():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        
        total_score = (science+maths+c+data_science)/4
    return redirect(url_for('successres', score=total_score))
    
if __name__ == "__main__":
    app.run(debug=True)