import json

from os import path

from flask import Blueprint, current_app, render_template, send_from_directory, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from server.models.user import User
from server.views.forms.login import LoginForm
from server.views.forms.reset_password import ResetPasswordRequestForm, ResetPasswordForm
from server.views.forms.register import RegistrationForm
from server.mail.password_reset import send_password_reset_email
from server.database import db


def jsonResponse(dictionary, status_code):
    return current_app.response_class(
            response=json.dumps(dictionary),
            status=status_code,
            mimetype='application/json'
            )


home = Blueprint('home', __name__, url_prefix='', template_folder='templates')


@home.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('home.login'), code=302)


@home.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('webapp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('home.login'))

        else:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('webapp.index'))
    else:
        return render_template('login.html', title='Sign In', form=form)


@home.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('home.index'))


@home.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home.login'))
    return render_template('register.html', title='Register', form=form)


@home.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
            return redirect(url_for('home.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('home.login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@home.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('home.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        return redirect(url_for('home.index'))
    return render_template('reset_password.html', form=form)


@home.route('/assets/<path:filename>', methods=['GET', 'POST'])
def send(filename):
    # TODO: figure out better way of serving static files, this is ghetto af...
    return send_from_directory(
            path.join(
                current_app.config['BASE_DIR'],
                "client/webapp/build/"
                ),
            filename
            )
