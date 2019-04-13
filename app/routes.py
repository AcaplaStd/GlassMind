from flask import render_template, send_from_directory, flash, redirect, url_for, request
from . import app, db
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from .models import User
from werkzeug.urls import url_parse


def render_template_params(template_name_or_list, **context):
    return render_template(template_name_or_list, is_whitemode=False, **context)


@app.route('/')
@app.route('/index')
def index():
    return render_template_params('home_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash('Login success!')
        return redirect(next_page)
    return render_template_params('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template_params('register.html', title='Register', form=form)


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)
