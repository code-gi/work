# from authors_app import db
from datetime import datetime
from authors_app.extensions import db

class User(db.Model):
    __tablename__="users"
    
    id =db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False,unique=True)
    contact=db.Column(db.Integer,unique=True)
    user_type=db.Column(db.String(100),nullable=False)
    image=db.Column(db.String(255),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now())
    updated_at=db.Column(db.DateTime,onupdate=datetime.now())
    #books=db.relationship('Book',backref='user')
