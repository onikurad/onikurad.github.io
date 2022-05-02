from re import L
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    title= "FizzBuzz welcome page"
    
    return render_template('main.html', title=title )

@app.route('/fizzbuzz/<int:lastnum>')
def fizzbuzz(lastnum):
    l=list (range (1,lastnum+1))
    
    return render_template('num.html', last_number=lastnum, numbers=l)