from os import path
import json

from flask import Blueprint, current_app, render_template, send_from_directory, request, redirect, url_for
from flask_login import login_user, current_user

from server.models.user import User
from server.views.forms.reset_password import ResetPasswordForm
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
    return render_template('index.html')


@home.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()
    if current_user.is_authenticated:
        return jsonResponse(
                {
                    'username': 'already logged in',
                    'password': 'already logged in'
                    },
                200
                )
    elif user is None:
        return jsonResponse(
                {'username': 'username does not exist'},
                400
                )
    elif not user.check_password(password):
        return jsonResponse(
                {'password': 'username and password do not match'},
                400
                )
    else:
        login_user(user)
        return jsonResponse(
                {
                    'username': 'login success',
                    'password': 'login success'
                    },
                200
                )


@home.route('/reset_password_request', methods=['POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return jsonResponse(
                {'password_reset': 'user is already logged in'},
                400
                )
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        send_password_reset_email(user)
        return jsonResponse(
                {'password_reset': 'check your mail for instructions'},
                200
                )
    else:
        return jsonResponse(
                {'email': 'email not found'},
                400
                )


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
                "client/web-app/build/"
                ),
            filename
            )
