import os
import unittest
from config import basedir
from app import app
from models import Users
from flask_login import current_user

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'testing'
        
        self.app = app.test_client()

        self.assertEqual(app.debug, False)
        
    def tearDown(self):
        pass

    #Tests
    def register(self, uname, pword, mfa):
        return self.app.post('/register', data = dict(uname = uname, pword = pword, mfa = mfa), follow_redirects = True) 

    def login(self, uname, pword, mfa):
        return self.app.post('/login', data=dict(uname=uname, pword=pword, mfa=mfa), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_register(self):
        response = self.register('test@nyu.edu', 'password', '000000000')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)
    
    def test_login(self):
        response = self.login('test@nyu.edu', 'password', '000000000')
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
