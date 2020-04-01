from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from routes import *

app = Flask(__name__)
api = Api(app)
app.config.from_object('config')

initalizeRoutes(api)
db = SQLAlchemy(app)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()