from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class CustomerForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    membership = IntegerField('Membership', validators=[DataRequired()])
    submit = SubmitField('Save')
