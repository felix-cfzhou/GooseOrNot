from os import path
from flask import Blueprint, current_app, render_template, send_from_directory


home = Blueprint('home', __name__, url_prefix='', template_folder='templates')


@home.route('/')
def show():
    return render_template('index.html')


@home.route('/assets/<path:filename>')
def send(filename):
    # TODO: figure out better way of serving static files, this is ghetto af...
    return send_from_directory(
            path.join(
                current_app.config['BASE_DIR'],
                "client/web-app/build/"
                ),
            filename
            )
