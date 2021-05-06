from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, logging
                                #change this after deploy
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)


#configurations
app.config['SECRET_KEY'] = 'Some really relevant sequency of characters, much better than this one.'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#Set Database 
db = SQLAlchemy(app)

if not os.path.exists('sample/data.db'):
    try:
        db.create_all()
        logger.info('Database created!')
    except:
        logger.critical('Database could NOT be created!')
