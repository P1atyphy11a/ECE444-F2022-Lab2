import email
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
bootstrap = Bootstrap(app)
moment = Moment(app)

class Form(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # email = StringField('What is your UofT Email address?', validators=[DataRequired(),Email(message="Please include an '@' in the email address.")])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name,current_time=datetime.utcnow())

@app.route('/invalid')
def invalid():
    return render_template('404.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    email = None
    form = Form()
    if form.validate_on_submit():
        old_name = session.get('name')
        # old_email = session.get('email')
        if old_name is not None and old_name!= form.name.data:
            flash('Looks like you have changed your name!')
        # if old_email is not None and old_email!= form.email.data:
        #     flash("Looks like you have changed your email!")
        session['name'] = form.name.data
        # if form.email.data.__contains__('utoronto'):
        #     session['email'] = form.email.data
        # else:
        #     session['email'] = ''
        return redirect(url_for('form'))
    return render_template('form.html',form=form,name=session.get('name'))

    # (not form.email.data.__contains__("@mail.utoronto.ca"))