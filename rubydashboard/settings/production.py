from rubydashboard.settings.common import *

import os

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False

ALLOWED_HOSTS = ['ruby.deadtired.me', 'localhost']
