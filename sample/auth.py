from flask import request, flash, redirect, url_for, Blueprint
from sample import db, models, views, app
from sample.models import User
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, login_required, logout_user, current_user
import logging


logging.basicConfig(filename='server.log', level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

auth = Blueprint('auth', __name__)
#https://www.youtube.com/watch?v=dam0GPOAvVI&t=1815s&ab_channel=TechWithTim

#validation and registration
@auth.route('/signup', methods=['POST', 'GET'])
def sign_up():
    logging.debug('function is working')
    if request.method == 'POST':
        #variables
        password = request.form.get('password') 
        conf = request.form.get('confirm-password')
        username = request.form.get('username')
        logging.debug(f'{username}, {password}, {conf}')

        user = User.query.filter_by(username=username).first()
        #equal passwords
        if user:
            flash('This username already exists')
            logging.debug('This username already exists')
        #password lenght
        elif len(password) < 8: 
            logging.debug('password too short')
            flash('password too short', category='error')
        elif len(password) > 12:
            logging.warn('password too long')
            flash('password too long', category='error')
        #username lenght
        elif len(username) < 3:
            logging.debug('username is too short')
            flash('username is too short', category='error')
        elif len(username) > 15:
            logging.warn('username is too long')
            flash('username is too long', category='error')
        elif password != conf:
            logging.debug('passwords do not match')
            flash('passwords do not match', category='error')
        else:
            new_user = User(username=username, password= generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            logging.debug(f'{User.query.all()}')
            flash('Account created!', category= 'success')
    return views.signup()

#checklogin 
@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
                    #SqlAlchemy stuff
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in succesfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('auth.secret_page'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Username does not exist', category='error')

    return views.index()

@auth.route('/secret_page')
def secret_page():
    
    return views.secret_page()

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
