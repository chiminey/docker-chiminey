import djcelery
from datetime import timedelta
import os

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('DB_ENV_POSTGRES_PASSWORD', ''),
        'HOST': 'db',
        'PORT': '5432',
    },
}

DEBUG = os.environ.get('DJANGO_DEBUG', 'False')
TEMPLATE_DEBUG = DEBUG

STAGING_PATH = "/staging"
DEFAULT_STORAGE_BASE_DIR = "/store"

OUR_APPS = ('chiminey.smartconnectorscheduler',
    'chiminey.simpleui')

INSTALLED_APPS = (
    'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    #'django.contrib.markup',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'storages',
    'djcelery',
    #'djkombu',
    'tastypie',
    'widget_tweaks',
    'httpretty',
    'mock',
    'south',
    'django_nose',
) + OUR_APPS

APIHOST = os.environ.get('APIHOST', 'http://127.0.0.1')


BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
REDIS_HOST = "redis"



CSRACK_USERDATA = """#!/bin/bash
chmod 700 /etc/sudoers
sed -i '/requiretty/d' /etc/sudoers
chmod 440 /etc/sudoers
echo changedsudo
"""

# According to Nectar Image Catalog 30/6/15
VM_IMAGES = {
              #'csrack': {'placement': None, 'vm_image': "ami-00000004", 'user_data': CSRACK_USERDATA},
              'csrack': {'placement': None, 'vm_image': "ami-00000009", 'user_data': CSRACK_USERDATA}, # centos 7
              #'nectar': {'placement': None, 'vm_image': "ami-00001c06", 'user_data': ''},
              #'nectar': {'placement': None, 'vm_image': "ami-00001e2b", 'user_data': ''},
              'nectar': {'placement': 'monash-01', 'vm_image': "ami-000022b0", 'user_data': ''}, # centos 7
              'amazon': {'placement': '', 'vm_image': "ami-9352c1a9", 'user_data': ''}}


LOGGER_LEVEL = "DEBUG"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'timestamped': {
            'format': ' [%(asctime)s: %(levelname)s/%(processName)s] %(message)s'
           # 'format': '%(asctime)s-%(filename)s-%(lineno)s-%(levelname)s: %(message)s'
        },
    },

    'handlers': {
    'file': {
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': os.path.join("/logs", os.environ.get('CHIMINEY_LOG_FILE', 'chiminey.log')),
    'formatter': 'timestamped',
            'maxBytes': 1024 * 1024 * 100,  # 100 mb
            'backupCount': 4
            },
    },
    'loggers': {

    'chiminey': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.smartconnectorscheduler': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.sshconnection': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.platform': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.cloudconnection': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.reliabilityframework': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.simpleui': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.mytardis': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.simpleui.wizard': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.storage': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.sshconnector': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.core': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'chiminey.smartconnectorscheduler.tasks': {
    'level': LOGGER_LEVEL,
    'handlers': ['file'],
    },
    'celery.task': {
    'level': 'ERROR',
    'handlers': ['file'],
    },
    'django.db.backends': {
    'level': 'ERROR',
    'handlers': ['file'],
    },
    'south': {
     'level': LOGGER_LEVEL,
     'handlers': ['file'],

    },
    }
    }


CELERYBEAT_SCHEDULE = {
    # "test": {
    #     "task": "smartconnectorscheduler.test",
    #     "schedule": timedelta(seconds=15),
    # },
    "run_contexts": {
        "task": "smartconnectorscheduler.run_contexts",
        "schedule": timedelta(seconds=int(os.environ.get('CELERY_POLL_TIME', 60)))
      },
    }


djcelery.setup_loader()


