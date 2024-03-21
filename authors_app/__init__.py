from flask import Flask
from app.extensions import db
from app.controllers.auth.auth_controllers import auth
from flask_migrate import Migrate
from app.extensions import migrate


from os import path
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)  #-app -db , object parameters


    from app.models.users import User
    from app.models.companies import Company
    from app.models.books import Book

    app.register_blueprint(auth, url_prefix="/api/v1/auth")

    @app.route("/")
    def home():
        return "Authors API project setup"

    return app
