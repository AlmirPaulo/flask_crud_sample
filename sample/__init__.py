from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os, logging

logging.basicConfig(level=logging.DEBUG, filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

#Set Database 
db = SQLAlchemy()
app = Flask(__name__)

def create_app():
    from sample import views, models, auth
    from sample.auth import auth
    from sample.models import User
    #configurations
    app.config['SECRET_KEY'] = 'Some really relevant sequency of characters, much better than this one.'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(app)
    
    #Create database
    if not os.path.exists('sample/data.db'):
        try:
            db.create_all()
            logging.info('Database created!')
        except:
            logging.critical('Database could NOT be created!')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    app.register_blueprint(auth, url_prefix='/auth')

    sample_app = app

    return sample_app

