from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# This file is for App configurations.

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///predictions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)