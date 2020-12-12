# app/models.py
from datetime import datetime
from yourapp import db

helper = db.Table("helper",
    db.Column("todo_id", db.Integer, db.ForeignKey("todo.id")),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
)

class Todo(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True, unique=True)
   description = db.Column(db.String(200), index=True, unique=True)
   user = db.relationship("User", secondary=helper, backref="task", lazy="dynamic")
#    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   done = db.relationship("Done", backref="task", lazy="dynamic")
   
   def __str__(self):
       return f"<Name {self.name}>"

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   user = db.Column(db.Text)
   todo = db.relationship("Todo", secondary=helper, backref="author", lazy="dynamic")
#    todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

   def __str__(self):
       return f"<User {self.user}>"

class Done(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   done = db.Column(db.Boolean, unique=True, default=True)
   todo_id = db.Column(db.Integer, db.ForeignKey('todo.id'))

   def __str__(self):
       return f"<User {self.done}>"