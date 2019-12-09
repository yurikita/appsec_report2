from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users():
    def __init__(self):
        self.Users = {}

    def check_user(self, uname):
        if uname in self.Users:
            return True
        else:
            return False

    def add_user(self, uname, pword, mfa):
        if(~self.check_user(uname)):
            self.Users[uname] = User(uname, pword, mfa)

class User(UserMixin):
    def __init__(self, uname, pword, mfa):
        self.id = uname
        self.pword = generate_password_hash(pword)
        self.mfa = mfa

    def is_authenticated(self):
        return True

    def check_password(self, pword):
        return check_password_hash(self.pword, pword)
