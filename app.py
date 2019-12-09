from flask import Flask, request, render_template, session, redirect
from config import Config
from forms import LoginForm, RegistrationForm, SpellCheckForm
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from models import User, Users
import subprocess

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.init_app(app)

USERS = Users()

@login.user_loader
def load_user(username):
    if USERS.check_user(username):
        return USERS.Users[username]
    else:
        return None

@app.route('/')
@app.route('/index')
def index():
    if not current_user.is_authorized():
        return redirect('/login')
    else:
        return redirect('/spell_check')

@app.route('/spell_check', methods = ['POST', 'GET'])
@login_required
def spell_check():
    form = SpellCheckForm()
    textout = ''
    misspelled = ''
    if form.validate_on_submit():
        inputtext = form.inputtext.data
        with open("inputtext.txt", "w") as f:
            f.write(inputtext)
            f.close()
            temp = subprocess.check_output(["./a.out", "inputtext.txt", "wordlist.txt"])
            temp = temp.decode()
            misspelled = temp.replace('\n', ', ')[:-2]
            textout = inputtext
    return render_template('spell_check.html', title = 'Spell Check', form = form, textout = textout, misspelled = misspelled)

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    logout_user()
    return redirect('/login')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    success = ''
    if form.validate_on_submit():
        uname = form.uname.data
        pword = form.pword.data
        mfa = form.mfa.data
        if USERS.check_user(uname):
            success = 'failure'
        else:
            USERS.add_user(uname, pword, mfa)
            success = 'success'
    return render_template('register.html', title = 'Register', form = form, success = success)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    result = ''
    if form.validate_on_submit():
        uname = form.uname.data
        pword = form.pword.data
        mfa = form.mfa.data
        if not USERS.check_user(uname):
            result = 'Incorrect'
        else:
            user = USERS.Users[uname]
            if not user.check_password(pword):
                result = 'Incorrect'
            elif not mfa == user.mfa:
                result = "Two-factor failure"
            else:
                result = 'Success'
                login_user(user)
    return render_template('login.html', title='Sign In', form=form, result = result)

if __name__ == '__main__':
    app.run(debug=True)
