from flask_mail import Mail, Message


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
