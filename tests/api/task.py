def test_task_enqueue(client, logged_in_user, image):
    client.post(
            '/api/login',
            data=dict(
                username='username',
                password='password'
                )
            )
    response = client.post(
            '/api/task',
            data=dict(
                image_id=image.id
                )
            )

    json = response.get_json()

    assert(isinstance(json['id'], str))
    assert(json['image_id'] == image.id)
