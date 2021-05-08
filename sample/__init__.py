from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
                                #change this after deploy
logging.basicConfig(level=logging.DEBUG, filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')
#logger = logging.getLogger(__name__)

app = Flask(__name__)


#configurations
app.config['SECRET_KEY'] = 'Some really relevant sequency of characters, much better than this one.'

#tentar reconfigurar com mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

#Set Database 
db = SQLAlchemy(app)

