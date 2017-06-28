import json

from flask import Blueprint
from flask import jsonify
from flask import request

from theSwitchAPI.services.authenticate_account import account_auth

authentication_endpoint = Blueprint('authentication', __name__, url_prefix='/api/v1/authenticate')


@authentication_endpoint.route('', methods=['POST'])
def authenticate_account():
    credential = json.loads(request.get_json())
    account = account_auth(credential)
    if account:
        return jsonify(account=account.to_json(), valid=200), 200
    else:
        return jsonify(error=404), 404
