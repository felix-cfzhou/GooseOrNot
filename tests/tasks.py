from uuid import uuid4

from server.tasks import delay
from server.tasks.predict import task_is_goose
from server.models.task import Task


def test_async_delay(queue):
    job = queue.enqueue(delay, args=(1,))

    assert(job.is_finished)


def test_task_is_goose(
        client,
        queue,
        session,
        logged_in_user,
        image,
        goose_pic_filename,
        requests_mock
        ):

    goose_bin_str = open(goose_pic_filename, 'rb').read()
    requests_mock.get(
            'http://example.com/goose_canada.jpg',
            content=goose_bin_str
            )

    job_id = str(uuid4())
    task = Task(
            id=job_id,
            name='task_is_goose',
            description='predict if image is of a goose or not',
            user_id=logged_in_user.id,
            image_id=image.id,
            )
    session.add(task)
    session.commit()

    job = queue.enqueue_call(
            func=task_is_goose,
            args=(image,),
            job_id=job_id
            )

    assert(job.is_finished)
    assert(task.complete)
    assert(image.is_goose)

    session.delete(task)
    session.commit()
