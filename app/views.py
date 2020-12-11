from flask import request, render_template, redirect, url_for

from app.forms import TodoForm
# from app.models import todos
# from app.models import todossqlite
# from app import app

from app import app, db
from app.models import Todo, User, Done

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Todo": Todo,
       "User": User,
       "Done": Done
   }

# app.config["SECRET_KEY"] = "nininini"

# @app.route("/todos/", methods=["GET", "POST"])
# def todos_list():
#     form = TodoForm()
#     error = ""
#     if request.method == "POST":
#         if form.validate_on_submit():
#             todossqlite.create(form.data)
#         return redirect(url_for("todos_list"))

#     return render_template("todos.html", form=form, todos=todossqlite.get_all(), error=error)


# @app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
# def todo_details(todo_id):
#     todo = todossqlite.get(todo_id)
#     form = TodoForm(data=todo)

#     if request.method == "POST":
#         if form.validate_on_submit():
#             todossqlite.update(todo_id, form.data)
#         return redirect(url_for("todos_list"))
#     return render_template("todo.html", form=form, todo_id=todo_id)


