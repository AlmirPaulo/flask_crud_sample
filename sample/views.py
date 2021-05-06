from flask import render_template
from sample import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    return render_template('signup.html')
