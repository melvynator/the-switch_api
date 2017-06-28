# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from theSwitchAPI.controllers.accounts.accounts import accounts_endpoint
from theSwitchAPI.controllers.accounts.authentification import authentication_endpoint

# Sample HTTP error handling
@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

# Register blueprint(s)
app.register_blueprint(accounts_endpoint)
app.register_blueprint(authentication_endpoint)


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
