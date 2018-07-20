from server.database import db

from flask import current_app
import redis
import rq


class Task(db.model):
    __tablename__ = 'tasks'

    id = db.Column(
            db.String(),
            primary_key=True,
            nullable=False
            )
    name = db.Column(
            db.String(),
            index=True,
            nullable=False
            )
    description = db.Column(
            db.String()
            )
    complete = db.Column(
            db.Boolean,
            default=False,
            )
    created = db.Column(
            db.DateTime(),
            default=db.func.now()
            )
    updated = db.Column(
            db.DateTime(),
            default=db.func.now(),
            onupdate=db.func.now()
            )

    def get_rq_job(self):
        try:
            rq_job = rq.job.Job.fetch(
                    self.id,
                    connection=current_app.redis
                    )
        except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
            return None
        return rq_job

    def get_progress(self):
        job = self.get_rq_job()
        return job.meta.get('progress', 0) if job is not None else 100
