from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import File

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
@login_required
def home():
    files = db.session.query(File.filename, File.camera_id, File.startat, File.endat).all()
    return render_template("home.html", user=current_user, data=files)
