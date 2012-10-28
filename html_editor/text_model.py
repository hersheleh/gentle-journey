from database import db
from flask.ext.sqlalchemy import SQLAlchemy

class Text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    tag = db.Column(db.String())
    
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag

    def edit(text):
        self.text = text
        
