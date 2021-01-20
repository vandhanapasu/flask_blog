from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '1c8b9ca15777561f1c757f1f722e41e5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site:db'

db = SQLAlchemy(app)

from Flask_blog import routes