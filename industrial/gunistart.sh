#!/bin/bash
 
NAME="hello_app" # Name of the application
DJANGODIR=/var/django/eve-industrial/industrial # Django project directory
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=industrial.settings # which settings file should Django use
DJANGO_WSGI_MODULE=industrial.wsgi # WSGI module name
 
echo "Starting $NAME as `whoami`"
 
# Activate the virtual environment
cd $DJANGODIR
source ../env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--workers $NUM_WORKERS \
--bind=0.0.0.0:9000 \
--log-level=debug \