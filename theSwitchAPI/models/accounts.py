# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from .. import db

from theSwitchAPI.lib.secure_db import SecureDB
import json


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


# Define a User model
class Account(Base):

    __tablename__ = 'auth_user'

    first_name = db.Column(db.String(128),  nullable=False)
    last_name = db.Column(db.String(128),  nullable=False)
    email = db.Column(db.String(128),  nullable=False, unique=True, primary_key=True)
    password = db.Column(db.String(192),  nullable=False)

    # New instance instantiation procedure
    def __init__(self, first_name=first_name, last_name=last_name, email=email, password=password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.create_password(password)

    def create_password(self, password):
        self.password = SecureDB.hash_password(password)

    def verify_password(self, try_password):
        return SecureDB.verify_password(self.password, try_password)

    def to_json(self):
        return json.dumps({"first name": self.first_name, "last name": self.last_name, "email": self.email})

    def __repr__(self):
        return '<Account {0}, {1}>'.format(self.first_name, self.last_name)
