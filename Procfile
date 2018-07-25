web: bin/start-nginx bin/start-pgbouncer gunicorn -c gunicorn.conf "server.factory:create_app()"
worker: bin/start-pgbouncer python -m server.worker
