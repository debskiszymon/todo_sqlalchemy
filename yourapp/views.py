from flask import request, render_template, redirect, url_for
from yourapp.forms import TodoForm, UserForm, UserTodoForm, TodoFormDone
from yourapp import app, db
from yourapp.models import Todo, User, Done

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Todo": Todo,
       "User": User,
       "Done": Done,
       "TodoForm": TodoForm
   }

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    todo_form = TodoForm()
    todo_form.user.choices = [(user.id, user.user) for user in User.query.all()]
    user_form = UserForm()
    error = ""
    if request.method == "POST":
        if todo_form.validate_on_submit():
            u = User.query.filter_by(id=todo_form.user.data).first()
            new_todo = Todo(name=todo_form.name.data, description=todo_form.description.data, author=[u])
            new_done = Done(done=todo_form.done.data, task=new_todo)
            db.session.add(new_done)
            db.session.add(new_todo)
            db.session.commit()

        elif user_form.validate_on_submit():
            new_user = User(user=user_form.user.data)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for("todos_list"))
    return render_template("todos.html", todo_form=todo_form, user_form=user_form, todos=Todo.query.all(), users=User.query.all(), dones=Done.query.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = Todo.query.get(todo_id)
    todo_form = TodoFormDone(obj=todo)

    if request.method == "POST":
        if todo_form.validate_on_submit():
            todo.name = todo_form.name.data
            todo.description = todo_form.description.data
            done = Done.query.get(todo_id)
            done.done = todo_form.done.data
            done.task = todo
            db.session.add(todo)
            db.session.add(done)
            db.session.commit()

        return redirect(url_for("todos_list"))
    return render_template("todo.html", todo_form=todo_form, todo_id=todo_id)

@app.route("/todos/user/<int:user_id>/", methods=["GET", "POST"])
def user_details(user_id):
    user_todo_form = UserTodoForm()
    user_todo_form.user.choices = [(user.id, user.user) for user in User.query.all()]
    user_todo_form.name.choices = [(todo.id, todo.name) for todo in Todo.query.all()]

    if request.method == "POST":
        if user_todo_form.validate_on_submit():
            u = User.query.get(user_id)
            t = Todo.query.filter_by(id=user_todo_form.name.data).first()
            u.task.append(t)
            db.session.add(u)
            db.session.commit()

        return redirect(url_for("todos_list"))
    return render_template("user.html", user_todo_form=user_todo_form, user_id=user_id)


