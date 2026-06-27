ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'staticfiles'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
INSTALLED_APPS = [
    ...
    'assets',
]

TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']

STATIC_URL = 'static/'
