web: bin/start-nginx bin/start-pgbouncer gunicorn -c config/gunicorn.conf --worker-class eventlet -w 1 "server.factory:create_app()"
worker: bin/start-pgbouncer python -m server.worker
