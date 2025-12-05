"""
Local settings that override production settings.
"""
import os
from .settings import *

# Правильные хосты
ALLOWED_HOSTS = [
    '81.30.105.18',
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
]

# CSRF настройки
CSRF_TRUSTED_ORIGINS = [
    'http://81.30.105.18',
    'https://81.30.105.18',
]

# Отладка
DEBUG = True

# Отключаем security для HTTP
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
