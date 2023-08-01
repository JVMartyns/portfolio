from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = [
    '.jvmartyns.com.br',
]

# S3 settings
DEFAULT_FILE_STORAGE = 'core.storage_backends.PublicMediaStorage'
STATICFILES_STORAGE = 'core.storage_backends.PublicStaticStorage'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']

# SMTP settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_RECEIVER = os.getenv('DEFAULT_RECEIVER')

CORS_ALLOWED_ORIGINS = [
    'https://portfolio.jvmartyns.com.br',
]

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
