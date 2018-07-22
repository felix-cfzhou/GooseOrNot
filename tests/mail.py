from server.mail import mail


def test_email_sending(app):
    with mail.record_messages() as outbox:
        mail.send_message(
                subject='testing',
                body='test',
                recipients=['example@example.com']
                )

        assert(len(outbox) == 1)
        assert(outbox[0].subject == 'testing')
        assert(outbox[0].body == 'test')
