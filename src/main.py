from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Todo
from . import db

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():    
        # todo_list = Todo.query.all()
    todo_list = Todo.query.filter_by(userId=current_user.id).all()
    print(todo_list)
    return render_template("index.html", todo_list=todo_list)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)