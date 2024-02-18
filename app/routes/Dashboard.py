from flask import Blueprint, render_template, request, redirect, url_for, flash
# from ..db import session 
# from ..models import UserModel
# from ..schemas import UserSchema
dashboard_blueprint = Blueprint('dashboard',__name__)

@dashboard_blueprint.route('/')
def index():
    return render_template('admins/index.html')

@dashboard_blueprint.route('/dashboard')
def dashboard():
    return render_template('base.html')