from server.models.task import Task


def test_task_model(session):
    task = Task(id='uuid', name='task')

    session.add(task)
    session.commit()

    assert(task.created is not None)
