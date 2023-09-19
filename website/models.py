from . import db 
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))


Base = declarative_base()

class File(Base):
    __tablename__ = "files"
    filename = db.Column(db.Text, nullable=False, primary_key=True)
    filetype = db.Column(db.Text, nullable=False)
    event = db.Column(db.Text, nullable=False)
    startat = db.Column(db.VARCHAR(40), nullable=False) 
    endat = db.Column(db.VARCHAR(40))
    camera_id = db.Column(db.Integer, nullable=False)
    flags = db.Column(db.Text, )
    timestamp = db.Column(db.VARCHAR(40)) 

class Event(Base):
    __tablename__ = "events"
    event = db.Column(db.Text, nullable=False)
    event_uid = db.Column(db.Integer, primary_key=True)
    startat = db.Column(db.VARCHAR(40), nullable=False)
    flags = db.Column(db.Text)
    timestamp = db.Column(db.VARCHAR(40))