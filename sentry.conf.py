#!/usr/bin/env python

import dj_database_url
import os

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': dj_database_url.config(default="postgres://localhost"),
}

SENTRY_KEY = os.environ.get('SENTRY_KEY', 'secret')

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_URL_PREFIX = 'http://gaslight-sentry.herokuapp.com'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ.get('PORT', 80)
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}

if 'MAIL_TO' in os.environ:
    ADMINS = [('J. Doe', os.environ['MAIL_TO'])]
    SENTRY_ADMINS = [os.environ['MAIL_TO']]

SERVER_EMAIL = os.environ.get('MAIL_FROM')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID')
GITHUB_API_SECRET = os.environ.get('GITHUB_API_SECRET')
GITHUB_EXTENDED_PERMISSIONS = ['repo']
