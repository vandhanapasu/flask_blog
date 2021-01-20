from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '1c8b9ca15777561f1c757f1f722e41e5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site:db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from Flask_blog import routes