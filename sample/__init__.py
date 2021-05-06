from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, logging
                                #change this after deploy
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

#configurations
app.config['SECRET_KEY'] = 'Some really relevant sequency of characters, much better than this one.'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#Set Database 
db = SQLAlchemy(app)

if not os.path.exists('sample/data.db'):
    db.create_all()
    logging.info('Database created!')
