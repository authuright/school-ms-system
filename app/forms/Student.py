from flask_wtf import Form
from wtforms import StringField, PasswordField

class LoginFormDemo(Form):
    username = StringField('username')
    password = PasswordField('password')