from flask import Blueprint, render_template, request

user_blueprint = Blueprint('user',__name__)


# Define your routes and views here
@user_blueprint.route('/register',methods=['GET', 'POST'])
def create():

    return render_template('auth/register.html')



@user_blueprint.route('/login')
def login():
    return render_template('auth/login.html')