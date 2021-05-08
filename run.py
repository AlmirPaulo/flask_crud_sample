from sample import app, views, models, auth
from sample.models import User 
import os, logging
 
logging.basicConfig(level=logging.DEBUG, filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

if not os.path.exists('sample/data.db'):
    try:
        db.create_all()
        logging.info('Database created!')
    except:
        logging.critical('Database could NOT be created!')

if __name__ == '__main__':
    app.run(debug=True)
