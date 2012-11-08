from database import db
from flask.ext.sqlalchemy import SQLAlchemy

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    price = db.Column(db.String())
    tag = db.Column(db.String())
    
    def __init__(self, title=None, body=None, price=None, tag=None):
        self.title = title
        self.body = body
        self.price = price
        self.tag = tag
        
    
