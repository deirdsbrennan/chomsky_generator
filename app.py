# -*- coding: utf-8 -*-
"""
Created on Tue May 19 03:26:58 2020

@author: Owner
"""

# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentences.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)

