from flask import Flask
import os
from src.config.config import Config
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Loading environment variables
load_dotenv()

# Declaring flask application
app = Flask(__name__)

# Calling the dev configuration
config = Config().dev_config

# Making the application use dev env
app.env = config.ENV

# Path for our mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")

# Track objects modifications and emit signals
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

# Sql Alchemy Instance
db = SQLAlchemy(app)

# Flask migrate instance to handle migrations
migrate = Migrate(app, db)

# Import models to let the migrate tool know
from src.models.architect import Architect
from src.models.project import Project
from src.models.bio import Bio
from src.models.admin import Admin

# Import api blueprint to register it with the app
from src.routes import api

app.register_blueprint(api, url_prefix="/api")
