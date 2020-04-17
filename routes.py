#region IMPORT
import csv
from flask import render_template, url_for, flash, redirect, request, jsonify
from application import app, db, bcrypt
from application.forms import LoginForm
from application.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
#endregion

#region Disctionaries practice ---> I will use this as source of feedback in a seperate page
tweets = [ 
{
    'author': 'Makabongwe Jussie Nkabinde',
    'title': 'Feedback 01',
    'content': 'I mean, 100%!',
    'date':'20 March 2020'
},
{
    'author': 'Sange Maxaku',
    'title': 'Feedback 02',
    'content': 'Weird design. Weak le app!',
    'date':'21 March 2020'
},
{
    'author': 'Neo Mokono',
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

@app.route("/design", methods = ['POST', 'GET'])
def design():      
    # first things first ...
    
    return render_template('design.html')
    
@app.route("/design_handle", methods =['GET', 'POST'])
def design_handle(): 
    if request.method == 'GET':
        flash('You have been logged in!', 'sucesss')   
        try:
            print("reached 1")
            f = 'words.txt'
            path = '/home/botlhale/Desktop/Athi/Application/words.txt'
            readFile = open(path)
            doc = readFile.readline()
            # write to the the html
            return render_template('design.html', text_read=doc)
        except:
            doc = ""     
    return redirect(url_for('design'))
    
@app.route("/feedback")
def feedback():
    return render_template('feedback.html', tweets = tweets)

@app.route("/save", methods = ['POST', 'GET'])
def save():    
    if request.method == 'POST':
        text = request.form['text']
        # [code for saving the file to the db fits here]
        flash('Successfully saved', 'sucesss')
    return redirect(url_for('design'))

@app.route("/login", methods = ['GET','POST'])
def login():
    if request.form == 'GET':
        print("Reached?")
    user1 = request.form['user']
    password1 = request.form['pass']
    
    if user1 and password1:
        newUser = user1[::-1]
        return jsonify({'user' : newUser})

    return jsonify({'error' : 'Incorrect username or password'})

    flash('Unsuccessful login. Please check your username and/or password', 'danger')      
    return render_template('login.html', title='Log In', form=form)
#endregion

@app.route("/logout")
def logout():
    #logout_user()
    return redirect(url_for('login'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
