from flask import render_template
from flask_login import login_required, current_user


def index():
    return render_template('index.html')

def signup():
    return render_template('signup.html')

@login_required
def secret_page():
    return render_template('secret_page.html', user=current_user)
