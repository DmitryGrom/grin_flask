from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # represent database object
migrate = Migrate(app, db) # represent migration mechanism

from app import routes, models
# models determines bd structure