#!/usr/bin/env sh
set -eu

MODULE_NAME=${MODULE_NAME:-"main"}
APP_NAME=${APP_NAME:-"app"}
export APP=${MODULE_NAME}:${APP_NAME}

export GUNICORN_CONFIG=${GUNICORN_CONFIG:-"gunicorn.conf.py"}

exec $@