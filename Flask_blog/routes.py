from flask import render_template, url_for, flash, redirect
from Flask_blog import app
from Flask_blog.forms import RegistrationForm, LoginForm
from Flask_blog.models import User, Post

posts = [
    {
        'author': 'vandhana',
        'title': 'first-blog',
        'content': 'first content',
        'date_posted': 'jan 17 2021'
    },
    {
        'author': 'sajji',
        'title': 'second-blog',
        'content': 'second content',
        'date_posted': 'jan 18 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
