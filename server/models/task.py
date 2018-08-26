from server.database import db

from flask import current_app
import redis
import rq


class Task(db.Model):
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
    user_id = db.Column(
            db.Integer,
            db.ForeignKey('users.id', name='FK_users_tasks')
            )
    image_id = db.Column(
            db.Integer,
            db.ForeignKey('images.id')
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

    def is_done(self):
        if self.complete:
            return True
        job = self.get_rq_job()

        if job is None:
            self.complete = True
            db.session.commit()
            return True

        return False
