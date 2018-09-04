from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from server.models.user import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate(self):
        if not FlaskForm.validate(self):
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user is None:
            self.username.errors.append('The username you have entered does not exist.')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('The username and password you entered does not match.')
            return False

        return True
