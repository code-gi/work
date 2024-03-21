from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# var  #constructor
db = SQLAlchemy()   #instances
migrate = Migrate()
bcrypt = Bcrypt()


# app = Flask(__name__)


# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager

# # Initialize SQLAlchemy and Migrate
# db = SQLAlchemy()
# migrate = Migrate()

# # Initialize Bcrypt
# bcrypt = Bcrypt()

# # Initialize JWTManager
# jwt = JWTManager()