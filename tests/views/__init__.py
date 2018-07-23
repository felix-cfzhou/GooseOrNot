import json


def post_json(client, path, dictionary):
    response = client.post(
            path,
            content_type='application/json',
            data=json.dumps(dictionary)
            )

    return response
