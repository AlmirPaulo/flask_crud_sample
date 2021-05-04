from flask import Flask

app = Flask(__name__)
app.config['SECRET-KEY'] = 'Some really relevant sequency of characters, much better than this one.'
