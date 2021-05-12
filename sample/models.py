from sample import db
from flask_login import UserMixin
import os, logging 

logging.basicConfig(level=logging.DEBUG, filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(12), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#Create database
if not os.path.exists('sample/data.db'):
    try:
        db.create_all()
        logging.info('Database created!')
    except:
        logging.critical('Database could NOT be created!')
