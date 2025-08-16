from flask import Flask,redirect,url_for

app = Flask(__name__) #WSGI APPLICATION used to communicate blw we server and web application

@app.route('/')# in home page
def welcome():
    return "welcome heha."
 
@app.route('/success/<int:score>')# building a dynamic URL with an integer variable
def success(score):
    return "the score is "+ str(score) 
 
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
 
 
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
