#!/usr/bin/env sh
set -eu

PRESTART_SCRIPT_PATH=/app/prestart.sh
if [ -f $PRESTART_SCRIPT_PATH ]; then
    echo "Found prestart script. Execute commands from it..."
    . $PRESTART_SCRIPT_PATH
fi

REQUIREMENTS_PATH=/app/requirements.txt
if [ -f $REQUIREMENTS_PATH ]; then
    echo "Found requirements.txt. Install packages..."
    pip install -r requirements.txt
fi

exec gunicorn -c $GUNICORN_CONFIG $APP
