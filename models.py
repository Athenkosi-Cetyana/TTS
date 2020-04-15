from datetime import datetime
from application import db
#from flask_login import UserMixin

print('2')
#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))

#region Model User
class User(db.Model):     
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg' )
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"       
#endregion

#region Model Post
#this defines the structure of the DB and is called a model that inherits from Model
class Post(db.Model): #what's in this function is what's returned when this model is invoked
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 

    def __repr__(self): #what's in this function is what's returned when this model is invoked
        return f"Post('{self.title}', '{self.date}')"
#endregion