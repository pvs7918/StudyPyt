from flask_wtf import FlaskForm



from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    full_name = StringField('Full Name', validators=[DataRequired()])
    e_mail = StringField('e-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmation_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
