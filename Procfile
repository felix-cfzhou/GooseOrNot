web: bin/start-nginx bin/start-pgbouncer-stunnel gunicorn -c gunicorn.conf "server.factory:create_app()"
worker: python -m server.worker
