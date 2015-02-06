# Simple Classroom
Simple Django application to handle all data from a classroom and his students.

## Requirements
* Python 2.7.x
* [Pip](https://pip.pypa.io/en/latest/installing.html)
* [Virtualenv and Virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
* SQLite or any DB supported by Django.

## Setup
Clone the repo
```
✗ git@github.com:maxicecilia/simple_classroom.git
✗ cd simple_classroom
```
Create and setup virtualenv (change paths to your convenience)
```
✗ mkvirtualenv classroom
✗ echo 'cd ~/code/simple_classroom' >> $WORKON_HOME/classroom/bin/postactivate
✗ echo 'export DJANGO_SETTINGS_MODULE=simple_classroom.settings' >> $WORKON_HOME/classroom/bin/postactivate
✗ echo 'unset DJANGO_SETTINGS_MODULE' >> $WORKON_HOME/classroom/bin/postdeactivate
✗ workok classroom
✗ pip install -r requirements.txt
✗ django-admin.py migrate
✗ django-admin.py runserver 0.0.0.0:8000
```

## Create admin user
Run this and follow the instructions
```
✗ django-admin.py createsuperuser
```
Use http://localhost:8000/admin/ to access the admin interface

## Need initial data?
Run this to load some!! (only ES data available)
```
✗ django-admin.py loaddata scripts/data/initial_data.json
```
