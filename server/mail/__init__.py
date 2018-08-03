from flask_mail import Mail, Message
from flask import current_app


mail = Mail()


def send_email(subject, recipients, text_body, sender=None, html_body=None):
    msg = Message(
            subject=subject,
            sender=sender,
            recipients=recipients,
            bcc=['gooseornot@gmail.com'],
            body=text_body,
            html=html_body,
            )

    mail.send(msg)


def send_async_email(subject, recipients, text_body, sender=None, html_body=None):
    current_app.task_queues['low'].enqueue_call(
            func=send_email,
            args=(
                subject,
                recipients,
                text_body,
                sender,
                html_body
                )
            )
