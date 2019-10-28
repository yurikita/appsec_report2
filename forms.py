from flask_wtf import FlaskForm
from wtforms import PasswordField, validators, IntegerField, StringField, SubmitField, TextAreaField

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    two_factor = StringField('Phone Number', [validators.DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    two_factor = StringField('Phone Number', [validators.DataRequired()])
    submit = SubmitField('Sign In')

class SpellCheckForm(FlaskForm):
    inputtext = TextAreaField('Input Text')
    submit = SubmitField('Submit')
