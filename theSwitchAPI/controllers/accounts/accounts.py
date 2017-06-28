import json

from flask import Blueprint
from flask import jsonify
from flask import request
from sqlalchemy.exc import IntegrityError

from theSwitchAPI.models.accounts import Account
from ... import db

accounts_endpoint = Blueprint('accounts', __name__, url_prefix='/api/v1/accounts')


@accounts_endpoint.route('/<string:email>', methods=['GET'])
def is_present(email):
    user = Account.query.filter_by(email=email).first()
    if user:
        print(user)
        return jsonify(user=user.to_json()), 200
    else:
        return jsonify(error=401), 401


@accounts_endpoint.route('', methods=['POST'])
def new_user():
    user_json = request.get_json()
    first_name = user_json.get('first_name')
    last_name = user_json.get('last_name')
    email = user_json.get('email')
    password = user_json.get('password')
    try:
        account = Account(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(account)
        print(account.to_json())
        db.session.commit()
        return jsonify(), 200
    except IntegrityError:
        print("integrity error")
        return jsonify(error=409), 409