import flask
from flask import Flask
import json 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.api import API

app = Flask(__name__)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://orclsql:tan5321@127.0.0.1/flux'
app.debug=True
db = SQLAlchemy(app)
app.CSRF_ENABLED = False
db.init_app(app)
from app import views, models
api = API(app)

 

