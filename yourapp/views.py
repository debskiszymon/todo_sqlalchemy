from flask import request, render_template, redirect, url_for
from yourapp.forms import TodoForm, UserForm, DoneForm
# from app.models import todos
# from app.models import todossqlite
# from app import app

from yourapp import app, db
from yourapp.models import Todo, User, Done

# @app.shell_context_processor
# def make_shell_context():
#    return {
#        "db": db,
#        "Todo": Todo,
#        "User": User,
#        "Done": Done
#    }

# app.config["SECRET_KEY"] = "nininini"

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    todo_form = TodoForm()
    user_form = UserForm()
    done_form = DoneForm()
    error = ""
    if request.method == "POST":
        if todo_form.validate_on_submit():
            # new_user = User(user="Gosia")
            # db.session.add(new_user)
            # db.session.commit()
            u = User.query.get(2)
            new_todo = Todo(name=todo_form.name.data, description=todo_form.description.data, author=[u])
            db.session.add(new_todo)
            db.session.commit()

            # todossqlite.create(form.data)
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=todo_form, todos=Todo.query.all(), users=User.query.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todossqlite.get(todo_id)
    form = TodoForm(data=todo)

    if request.method == "POST":
        if form.validate_on_submit():
            todossqlite.update(todo_id, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


