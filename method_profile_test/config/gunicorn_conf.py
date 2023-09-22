"""gunicorn WSGI server configuration."""

bind = '0.0.0.0:9000'
worker_class = 'uvicorn.workers.UvicornWorker'
workers = 4
timeout = 60
graceful_timeout = 60
reload = False
accesslog = '-'
errorlog = '-'
daemon = False