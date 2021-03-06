# Django settings for surfnet project.
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_variable('ZUNDAPPDBNAME'),
        'USER': get_env_variable('ZUNDAPPDBUSER'),
        'PASSWORD': get_env_variable('ZUNDAPPDBPASSWORD'),
        'HOST': get_env_variable('DBHOST'),
        'PORT': get_env_variable('DBPORT'),
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_variable('SECRETKEY')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_ROOT.child('log') + "/zundapp.log",
            'maxBytes': 5000000,
            'backupCount': 10,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps.reports': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
        },
    }
}