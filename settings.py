ALLOWED_HOSTS = ['*']

STATIC_ROOT = BASE_DIR / 'staticfiles'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
