from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField(
            'Password',
            validators=[DataRequired()]
            )
    password2 = PasswordField(
            'Repeat Password',
            validators=[
                DataRequired(),
                EqualTo('password')
                ])
    submit = SubmitField('Reset Password')
