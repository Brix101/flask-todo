from flask import Blueprint ,render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Todo
from . import db

todo = Blueprint('todo', __name__)

@todo.route("/add", methods=["POST"])
@login_required
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title,userId=current_user.id, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.index"))


@todo.get("/update/<int:todo_id>")
def update(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("main.index"))


@todo.get("/delete/<int:todo_id>")
def delete(todo_id):
    # todo = Todo.query.filter_by(id=todo_id).first()
    todo = db.session.query(Todo).filter(Todo.id == todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("main.index"))