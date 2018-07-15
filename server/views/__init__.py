from os import environ, path
from flask import Blueprint, render_template, send_from_directory


home = Blueprint('home', __name__, url_prefix='', template_folder='templates')


@home.route('/')
def show():
    return render_template('index.html')


@home.route('/assets/<path:filename>')
def send(filename):
    return send_from_directory(
            path.join(
                environ['PROJECT_DIR'],
                "client/web-app/build/"
                ),
            filename
            )
