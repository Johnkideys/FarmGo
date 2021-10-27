from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from FlaskBlog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail()


#You don't have to use blueprints. Just import current_app as app in your routes.py and you are free to go.
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    with app.app_context():#Also, you have to add this to the factory (the create_app function) to register your routes:
        from FlaskBlog import routes

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    return app

