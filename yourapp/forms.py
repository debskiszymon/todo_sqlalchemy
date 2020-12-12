from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])

class UserForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])

class DoneForm(FlaskForm):
    done = BooleanField('done')
