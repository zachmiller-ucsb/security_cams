from flask import Blueprint, render_template, send_from_directory
from flask_login import login_required, current_user
from . import db
from .models import File

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
@login_required
def home():
    files = db.session.query(File.filename, File.camera_id, File.startat, File.endat).all()
    return render_template("home.html", user=current_user, data=files)

@views.route('/uploads/<path:filename>', methods=['GET'])
@login_required
def download_file(filename):
    return send_from_directory(directory='/Users/zachary/Desktop/security_cams/instance/video/', path=filename, as_attachment=True)
