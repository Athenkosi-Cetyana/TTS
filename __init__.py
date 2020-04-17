from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_assets import Bundle, Environment

#region Configurations  -------- wsgi_app = app.wsgi_app
app = Flask(__name__) # an instantiated Flask variable is contained in the application variable 
app.config['SECRET_KEY'] = 'dd629e01302dd66fafae953bcc8f3902' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # this makes a db associated with this program
bcrypt = Bcrypt(app) # passing the app to initialise this class
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

js = Bundle('p5.js','p5.min.js','alert_message.js','sketch.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', js)
#endregion

#region Avoiding-Circular-Importing
from application import routes
#endregion

#reading the text file
