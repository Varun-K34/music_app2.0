# app/routes.py
from flask import render_template, url_for, redirect, request
from app import app, db
from app.models import User, Song, Album

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Add more routes based on your requirements
