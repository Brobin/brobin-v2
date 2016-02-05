from django.core.wsgi import get_wsgi_application
import sys
import os


cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/brobin')

INTERP = os.path.expanduser("~/brobin.me/venv/bin/python")

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, '$HOME/brobin.me/venv/bin')
sys.path.insert(0, '$HOME/brobin.me/venv/lib/python3.4/site-packages/django')
sys.path.insert(0, '$HOME/brobin.me/venv/lib/python3.4/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "brobin.settings"
application = get_wsgi_application()
