# Gunicorn Server in Docker

This is a small and fast Docker image to fast deploy your applications via Gunicorn server.

All images are based on Python-Alpine images.

**GitHub Repository Page**: [https://github.com/iamelin/gunicorn-docker](https://github.com/iamelin/gunicorn-docker)

**Docker Hub Page**: [https://hub.docker.com/r/amelin/gunicorn](https://hub.docker.com/r/amelin/gunicorn)


## Supported tags

* python3.8
* python3.7
* python3.6


## Quick Start

Deploying your application is very simple! Just do the following:
1. Create a directory `app` with your Python application. The main file must be named `main.py`
and the WSGI callable must be named `app`.
2. Pull the image from Docker Hub:
```docker pull amelin/gunicorn:python3.8```
3. Create `Dockerfile` with the following content:

```
FROM amelin/gunicorn:python3.8

ADD ./app/ /app
```

That's all! Now build your image and start a new container. If the file /app/requirements.txt
exists, packages will be installed automatically before starting the application.
Then you can send requests to your application that listens port 5000.


## Configuration

You can configure Gunicorn and image using the following environment variables:
* `PORT` &mdash; port that the server listens (default value: `5000`)
* `WORKERS` &mdash; number of workers that handle requests (default value: number of cores
of your processor * 2 + 1)
* `LOGLEVEL` &mdash; level of logs (default value: `info`)
* `ACCESS_LOG` &mdash; file which the server writes access logs to (default no access logs)
* `ERROR_LOG` &mdash; file which the server writes error logs to (default value: `stdout`)
* `MODULE_NAME` &mdash; a Python module that contains a WSGI callable (default value: `main`,
file `main.py` in the working directory `/app`)
* `APP_NAME` &mdash; a WSGI callable which handles requests (default value: `app`)
* `GUNICORN_CONFIG` &mdash; a Python script that contains the configuration of a Gunicorn instance
(default value: `gunicorn.conf.py` in the working directory `/app`)
* `TZ` &mdash; timezone (default value: `UTC`)

Also the application directory `/app` contains the file `prestart.sh` that runs before starting
a container. You can use it to prepare your application to work (e.g. run migrations etc).
