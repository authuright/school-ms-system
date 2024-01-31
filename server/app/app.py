# third party import
import os
from flask import Flask, Blueprint,render_template
from os import environ
from flask_sqlalchemy import SQLAlchemy 

from .db import engine,Base
# package import
from .routes import user_blueprint, student_blueprint

app = Flask(__name__,template_folder='templates')  

# Register the user blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(student_blueprint, url_prefix='/student')

@app.route('/')
def basic():
    return render_template('admins/index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('base.html')
    
with app.app_context():
    Base.metadata.create_all(engine)