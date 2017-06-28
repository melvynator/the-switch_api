from theSwitchAPI.models.accounts import Account


def account_auth(credential):
    account = Account.query.filter_by(email=credential.get("email")).first()
    if account.verify_password(credential.get("password")):
        return account
    else:
        return None
