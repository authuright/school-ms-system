from flask import Blueprint, render_template, request

from ..db import session
from ..models import StudentModel
from ..schemas import StudentSchema

student_blueprint = Blueprint('student',__name__)


# Define your routes and views here
@student_blueprint.route('/',methods=['GET', 'POST'])
def allStudent():
    return render_template('admins/students.html')


@student_blueprint.route('/create', methods=['GET','POST'])
def newStudent():
    return render_template('admins/add-student.html')



@student_blueprint.route('/login')
def SingleStudent():
    return render_template('admins/login.html')