# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0609325/data/www/lenaphoto.worlddelete.ru/lena_photo')
sys.path.insert(1, '/var/www/u0609325/data/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'lena_photo.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


