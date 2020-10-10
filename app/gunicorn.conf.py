import json
import multiprocessing
import os

custom_bind = os.getenv("BIND", None)
host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "5000")
bind_val = custom_bind if custom_bind is not None else "{host}:{port}".format(host=host, port=port)

workers_val = os.getenv("WORKERS", multiprocessing.cpu_count() * 2 + 1)

loglevel_val = os.getenv("LOGLEVEL", "info")

accesslog_val = os.getenv("ACCESS_LOG", "None")
errorlog_val = os.getenv("ERROR_LOG", "-")

# Gunicorn config
bind = bind_val
workers = workers_val
loglevel = loglevel_val
accesslog = accesslog_val
errorlog = errorlog_val