## Integrate HTML with Flask
## HTTP verb GET and POST

## Jinja2 template engine
'''
{%....%} conditions, for loops
{{    }} expressions to print output
{#....#} comments
'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = 'pass'
    else:
        res = 'fail'
    exp = {'score':score,'res' : res}
    return render_template('result.html', result = exp)

@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has fail and the marks is ' + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'

    return redirect(url_for(result, score = marks))

@app.route('/submit', methods =['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        c = float(request.form['C'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience) / 4

    result = ""
    

    return redirect(url_for('success', score = total_score))


if __name__ == '__main__':
    app.run(debug = True)