web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn ladies_clothing.wsgi:application --bind 0.0.0.0:$PORT
