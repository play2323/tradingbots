DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'playarbitrage$smooth',
        'USER': 'playarbitrage',
        'PASSWORD': 'Mister@123',
        'HOST': 'playarbitrage.mysql.pythonanywhere-services.com',
        'PORT': '<database_port>',
    }
}

# Add the necessary apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'trading_bot',
]

# Add the necessary middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add other necessary settings
ROOT_URLCONF = 'trading_bot.urls'

# trading_bot/custom_auth_backend.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        else:
            return None


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'trading_bot.custom_auth_backend.CustomAuthenticationBackend',
]


SENTIMENT_IO_API_KEY = 'YOUR_API_KEY'

BINANCE_API_KEY = 'your_binance_api_key'
BINANCE_SECRET_KEY = 'your_binance_secret_key'


KRAKEN_API_KEY = 'your_kraken_api_key'
KRAKEN_SECRET_KEY = 'your_kraken_secret_key'

HUOBI_API_KEY = 'your_huobi_api_key'
HUOBI_SECRET_KEY = 'your_huobi_secret_key'

BITFINEX_API_KEY = 'your_bitfinex_api_key'
BITFINEX_SECRET_KEY = 'your_bitfinex_secret_key'

SLACK_WEBHOOK_URL = 'your_slack_webhook_url'
