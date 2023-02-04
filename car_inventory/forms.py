from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    #email, password, first_name, last_name
    email = StringField('Email', validators = [DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()


class CarForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    price = DecimalField('price', places = 2)
    color = StringField('color')
    model = StringField('model')
    year = IntegerField('year')
    mileage = StringField('mileage')
    cost_of_production = DecimalField('cost of production', places = 2)
    submit_button = SubmitField()