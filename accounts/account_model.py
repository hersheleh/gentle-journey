import os
import hashlib
from database import db
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
'''
Account Model module contains the code for manipulating account data.
This involves adding editing and deleting accounts
'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(800))
    salt = db.Column(db.String(512))

    def __init__(self, username, password):
        self.username = username
        self.salt = unicode(os.urandom(32), errors='ignore')
        self.password = self.encrypt(password, self.salt)

        
    def __repr__(self):
        return '<User %r>' % self.username

    
    def encrypt(self, password, salt):
        return hashlib.sha512(salt+password).hexdigest()
    
    
    def authenticate(self, username, password):
        if (self.username == username):
            if (self.encrypt(password, self.salt) == self.password):
                return True
            
        return False

