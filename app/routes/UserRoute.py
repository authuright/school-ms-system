from flask import Blueprint, render_template, request, redirect, url_for, flash, session
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


from sqlalchemy.orm.exc import NoResultFound

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    print("Starting Block")
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password') 
        print("Step 1: ", username, password)
        try:
            user = session.query(UserModel).filter_by(username=username, password=password).first()
            print("Step 2: ", user)
            if user:
                session['user_id'] = user.id
                session['username'] = user.username
                return redirect(url_for('dashboard.index'))
            else:
                return redirect(url_for('user.login'))
        except NoResultFound:
            print("No user found with the provided credentials.")
            return redirect(url_for('user.login'))
        except Exception as e:
            print("An error occurred:", e)
            # Handle the error appropriately, such as logging it or returning an error page
            return render_template('admins/error-404.html')

    return render_template('admins/login.html')