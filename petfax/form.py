from flask import (Blueprint, render_template)

bp3 = Blueprint('form', __name__)

@bp3.route('/')
def form():
    return render_template('form.html')