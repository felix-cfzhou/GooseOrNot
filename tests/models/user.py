from server.models.user import User


def test_user_model(session):
    user = User(
            username='david_duan98',
            email='david_duan98@example.com',
            )

    user.set_password('password')

    session.add(user)
    session.commit()

    assert(user.id > 0)
    assert(user.check_password('password'))
