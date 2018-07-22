from server.mail import mail, send_email


def test_email_config(app):
    with mail.record_messages() as outbox:
        mail.send_message(
                subject='testing',
                body='test',
                recipients=['example@example.com']
                )

        assert(len(outbox) == 1)
        assert(outbox[0].subject == 'testing')
        assert(outbox[0].body == 'test')


def test_send_email(app):
    with mail.record_messages() as outbox:
        send_email(
                subject='testing',
                text_body='test',
                recipients=['example@example.com']
                )

        assert(len(outbox) == 1)
        assert(outbox[0].bcc[0] == 'gooseornot@gmail.com')
