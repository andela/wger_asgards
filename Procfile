web:  invoke create_settings --settings-path ./settings.py; invoke bootstrap_wger --settings-path ./settings.py
--no-start-server; python manage.py collectstatic --noinput; gunicorn wger.wsgi --log-file -
