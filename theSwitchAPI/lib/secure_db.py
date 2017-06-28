import nacl.pwhash


class SecureDB:

    @staticmethod
    def hash_password(password):
        password_as_bytes = bytes(password, "utf-8")
        return nacl.pwhash.scryptsalsa208sha256_str(password_as_bytes)

    @staticmethod
    def verify_password(password, try_password):
        try:
            nacl.pwhash.verify_scryptsalsa208sha256(password, bytes(try_password, "utf-8"))
            return True
        except nacl.exceptions.InvalidkeyError:
            return False