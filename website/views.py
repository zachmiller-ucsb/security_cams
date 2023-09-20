from flask import Blueprint, render_template, send_from_directory, jsonify, url_for, request
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
def get_video(filename):
    return send_from_directory(directory='/Users/zachary/Desktop/security_cams/instance/video/', path=filename, as_attachment=True)

@views.route('/generate_url', methods=['POST'])
@login_required
def generate_url():
    data = request.get_json()
    filename = data['filename']
    url = url_for('views.get_video', filename=filename)
    return jsonify({'url': url})
