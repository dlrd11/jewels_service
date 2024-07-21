import pytest
import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewels_service.settings')


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
    settings.ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']


django.setup()
