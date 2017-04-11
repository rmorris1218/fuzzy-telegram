import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        debug = os.environ.get('FLASK_DEBUG')
        appfile = os.environ.get('FLASK_APP')
        secret = os.environ.get('SECRET_KEY')
        app_stage = os.environ.get('APP_STAGE')
        return "Hello CodePipeline! FLASK_DEBUG: {} FLASK_APP: {} SECRET_KEY: {}" \
        "APP STAGE: {}".format(
            debug, appfile, secret, app_stage
        )

    return app

def get_db(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}/{}".format(
        os.environ.get('RDS_HOSTNAME'), os.environ.get('RDS_DB_NAME')
    )
    db = SQLAlchemy(app)
    return db
