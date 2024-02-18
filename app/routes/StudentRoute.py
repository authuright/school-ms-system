from flask import Blueprint, render_template, request, redirect,url_for

from ..db import session
from ..models import StudentModel
from ..schemas import StudentSchema
# from ..forms import LoginFormDemo
student_blueprint = Blueprint('student',__name__)


# Define your routes and views here
@student_blueprint.route('/',methods=['GET', 'POST'])
def allStudent():
    # form = LoginFormDemo()
    return render_template('admins/students.html')


@student_blueprint.route('/create', methods=['GET','POST'])
def newStudent():
    if request.method == "POST":
        print("-----------form init--------------")
        user = request.form['fname']
        print(user)
        return redirect(url_for("student.user",usr=user))
    else:
        return render_template('admins/add-student.html')


@student_blueprint.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'


@student_blueprint.route('/login')
def SingleStudent():
    return render_template('admins/login.html')