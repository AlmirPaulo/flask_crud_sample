from flask import request, flash
from sample import db, models, views, app
from sample.models import User
from werkzeug.security import generate_password_hash
import logging

logging.basicConfig(filename='server.log', level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

#https://www.youtube.com/watch?v=dam0GPOAvVI&t=1815s&ab_channel=TechWithTim
# Hashing https://www.youtube.com/watch?v=UtF58KqcHWU&ab_channel=sentdex

#validation
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    logging.debug('function is working')
    if request.method == 'POST':
        #variables
        password = request.form.get('password') 
        conf = request.form.get('confirm-password')
        user = request.form.get('username')
        logging.debug(f'{user}, {password}, {conf}')
        #equal passwords
        if password != conf:
            logging.debug('passwords do not match')
            flash('passwords do not match', category='error')
        #password lenght
        elif len(password) < 8: 
            logging.debug('password too short')
            flash('password too short', category='error')
        elif len(password) > 12:
            logging.warn('password too long')
            flash('password too long', category='error')
        #username lenght
        elif len(user) < 3:
            logging.debug('username is too short')
            flash('username is too short', category='error')
        elif len(user) > 15:
            logging.warn('username is too long')
            flash('username is too long', category='error')
        else:
            new_user = User(username=user, password= generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            logging.debug(f'{User.query.all()}')
            flash('Account created!', category= 'success')
    return views.signup()

#registration

#checklogin 
