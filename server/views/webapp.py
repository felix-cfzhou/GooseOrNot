from flask import Blueprint, render_template
from flask_login import login_required


webapp = Blueprint('webapp', __name__, url_prefix='/webapp', template_folder='templates')


@webapp.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@webapp.route('/<path:path>', methods=['GET', 'POST'])
@login_required
def index(path):
    return render_template('index.html')
