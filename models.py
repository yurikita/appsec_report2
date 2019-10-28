from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users():
    def __init__(self):
        self.Users = {}

    def check_user(self, username):
        if username in self.Users:
            print('%s exists', username)
            return True
        else:
            print('%s does not exist', username)
            return False

    def add_user(self, username, password, two_factor):
        if(~self.check_user(username)):
            self.Users[username] = User(username, password, two_factor)
            print('Added user %s', username)
            print('Checking id %s', self.Users[username].id)

class User(UserMixin):
    def __init__(self, username, password, two_factor):
        self.id = username
        self.password = generate_password_hash(password)
        self.two_factor = two_factor

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return str(self.id)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
