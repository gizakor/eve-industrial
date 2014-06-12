killall gunicorn
gunicorn --workers=4 --bind=0.0.0.0:9000 industrial.wsgi:application --daemon

