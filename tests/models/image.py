from server.models.image import Image


def test_image_model(session):
    image = Image(
            file_name="testing_file_name",
            url="testing_url"
            )

    session.add(image)
    session.commit()

    assert(image.id > 0)
