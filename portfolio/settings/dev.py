from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0K$iK|"bsP4{<.br*itYB$)P8Ad#IIy#QLJfAtuYI/&;Y#(0V<G~N}euKklNc-GG'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
]

# SMTP settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
