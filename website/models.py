from . import db 
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))

class File(db.Model):
    __bind_key__ = 'motion'
    filename = db.Column(db.Text, nullable=False, primary_key=True)
    filetype = db.Column(db.Text, nullable=False)
    event = db.Column(db.Text, nullable=False)
    startat = db.Column(db.VARCHAR(40), nullable=False) 
    endat = db.Column(db.VARCHAR(40))
    camera_id = db.Column(db.Integer, nullable=False)
    flags = db.Column(db.Text, )
    timestamp = db.Column(db.VARCHAR(40)) 

class Event(db.Model):
    __bind_key__ = 'motion'
    event = db.Column(db.Text, nullable=False)
    event_uid = db.Column(db.Integer, primary_key=True)
    startat = db.Column(db.VARCHAR(40), nullable=False)
    flags = db.Column(db.Text)
    timestamp = db.Column(db.VARCHAR(40))