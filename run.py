from sample import create_app

#logging.basicConfig(level=logging.DEBUG, filename='server.log', format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

if __name__ == '__main__':
    create_app().run(debug=True)
