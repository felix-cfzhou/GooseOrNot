from server.tasks import delay


def test_async_delay(queue):
    job = queue.enqueue(delay, args=(1,))

    assert(job.is_finished)
