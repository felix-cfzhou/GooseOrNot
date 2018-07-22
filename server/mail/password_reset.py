from flask import render_template_string

from server.mail import send_email
from server.mail.templates.reset_password import reset_password


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(
            subject='[Goose Or Not] Reset Your Password',
            recipients=[user.email],
            text_body=render_template_string(
                reset_password,
                user=user,
                token=token
                )
            )
