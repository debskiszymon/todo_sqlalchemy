from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired
from yourapp import db
from yourapp.models import Todo, User, Done

class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    user = SelectField('user', choices=[])
    done = SelectField('done', choices=[("nie zrobione", "nie zrobione"), ("zrobione", "zrobione")])

class TodoFormDone(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    done = SelectField('done', choices=[("nie zrobione", "nie zrobione"), ("zrobione", "zrobione")])

class UserForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])

class UserTodoForm(FlaskForm):
    user = SelectField('user', choices=[])
    name = SelectField('name', choices=[])
