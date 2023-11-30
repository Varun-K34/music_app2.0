# app/models.py
from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other user fields

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other song fields

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other album fields
