import os
import sys
import site

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/root/.virtualenvs/facultad-prod/lib/python2.7/site-packages')

# sys.path.append('/home/shared/kobold/irongolem')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_classroom.settings")
# os.environ["DJANGO_SETTINGS_MODULE"] = "settings.base"

# Activate your virtual env
activate_env = os.path.expanduser("/root/.virtualenvs/facultad-prod/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
