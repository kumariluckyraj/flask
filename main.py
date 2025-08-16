# integrating html with flask
# http verb get and post
# jinja2 template engine
''' 
{%....%} for conditions, for loops
{{ }}expression to print output
{#....#}this is for comments

'''




from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__) #WSGI APPLICATION used to communicate blw we server and web application

@app.route('/')# in home page
def welcome():
    return render_template('index.html')  # Render the HTML template(index.html)
 
@app.route('/success/<int:score>')# building a dynamic URL with an integer variable
def success(score):
      res=""
      if score >= 50:
            res='PASS'
      else:   
            res='FAIL'
      exp={'score': score, 'res':res}         
      return render_template('result.html',result=exp)
 
@app.route('/fail/<int:score>')
def fail(score):
    return "the failed score is "+ str(score) 

# result checker
@app.route('/result/<int:marks>')
def results(marks):
    result=""
    if marks < 50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result, score=marks))         

# result checker submit html page
@app.route('/submit', methods=['POST','GET'])
def submit(): 
    total_score=0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        total_score = (science + maths + english)/4
    res=""
   
    return redirect(url_for('success', score=total_score))            
 
 
 
 
 
 
 
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
