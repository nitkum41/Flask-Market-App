from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import  LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# FOR DISPLAYING FORM
app.config['SECRET_KEY'] = '6d825a04bd7adc0a32ad3802' #self generated random key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page' #redirect user to login page when login_required decorator acts
login_manager.login_message_category = 'info'

from market import routes
