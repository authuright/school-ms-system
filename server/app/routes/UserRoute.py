from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..db import session 
from ..models import UserModel
from ..schemas import UserSchema
user_blueprint = Blueprint('user',__name__)


# Define your routes and views here
@user_blueprint.route('/register',methods=['GET', 'POST'])
def register():
    return render_template('admins/register.html')

@user_blueprint.route('/error',methods=['GET', 'POST'])
def notfound():
    return render_template('admins/error-404.html')


@user_blueprint.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username,password)
        users = session.query(UserModel).all() #filter all
        print("Users",users)
        user_schema = UserSchema()
        user_json = user_schema.dump(users, many=True) 
        print("Track 1 :",user_json)
        for data in user_json:
            user_data= {key: value for key, value in data.items()}
            print("User :: {} , Password {}".format(user_data['username'],user_data['password']))
            if user_data['username'] == username and user_data['password'] == password:
                return redirect(url_for('basic'))
            else:
                return redirect(url_for('user.login'))

    return render_template('admins/login.html')