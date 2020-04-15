#region IMPORT
from flask import  render_template, url_for, flash, redirect
from application import app, db, bcrypt
from application.forms import RegForm, LoginForm
from application.models import User, Post

#from flask_login import login_user, current_user, logout_user, login_required
#endregion
print('3')
#region Disctionaries practice ---> I will use this as source of feedback in a seperate page
tweets = [ 
{
    'author': '@maks',
    'title': 'Feedback 01',
    'content': 'I mean, 100%!',
    'date':'20 March 2020'
},
{
    'author': '@sange',
    'title': 'Feedback 02',
    'content': 'Weird design. Weak le app!',
    'date':'21 March 2020'
},
{
    'author': '@neo',
    'title': 'Feedback 03',
    'content': 'Uhm, could do better. I give it boma-4.5',
    'date':'22 March 2020'
}
]
#endregion

#region HTML - pages as templated
@app.route("/")
@app.route("/home")
def method():
    filename = "pic.jpg"
    return render_template('home.html', user_image = filename)

@app.route("/about")
@app.route("/contact-us")
def about():
    return render_template('about.html')

@app.route("/design")
def design():    
    flash('You are logged in', 'success')     
    return render_template('design.html')
    
@app.route("/design_handle", methods =['GET', 'POST'])
def design_handle(): 
    return redirect(url_for('design'))
    
@app.route("/feedback")
def feedback():
    return render_template('feedback.html', tweets = tweets)

@app.route("/register", methods =['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Acount created for {form.username.data}. You can now log in!', 'sucesss') 
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'a@botlhale.ai' and form.password == 'pass':
            flash('You have been logged in!', 'sucesss')         
            return redirect(url_for('design'))
        else:
            flash('Unsuccessful login. Please check your username and/or password', 'danger')      
    return render_template('login.html', title='Login', form=form)

#endregion

#@app.route("/logout")
#def logout():
#    logout_user()
#    return redirect(url_for('home'))

#@app.route("/account")
#@login_required
#def account():
#    return render_template('account.html', title='Account')
   
