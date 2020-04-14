from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#region Configurations
app = Flask(__name__) # an instantiated Flask variable is contained in the application variable 
app.config['SECRET_KEY'] = 'dd629e01302dd66fafae953bcc8f3902' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # this makes a db associated with this program
bcrypt = Bcrypt(app) # passing the app to initialise this class
#endregion

#region Avoiding-Circular-Importing
from app import routes
#endregion