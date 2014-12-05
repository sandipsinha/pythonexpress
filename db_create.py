from migrate.versioning import api
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path

db.create_all()
 