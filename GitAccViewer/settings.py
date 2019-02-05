import os
from configurations import Configuration, values


class Base(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!


    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        'allauth.account.auth_backends.AuthenticationBackend',
    )

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.github',
        'git_service',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'GitAccViewer.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')]
            ,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'GitAccViewer.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/2.1/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.1/howto/static-files/

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
    STATIC_URL = '/static/'

    SITE_ID = 1

    SOCIALACCOUNT_PROVIDERS = {
        'github': {
            'SCOPE': [
                'user',
                'repo',
                'read:org',
            ],
        }
    }

    LOGIN_REDIRECT_URL = '/'
    ACCOUNT_LOGOUT_ON_GET = True


class Dev(Base):
    SECRET_KEY = 'e847whc@45o$&z!aupzx7$4)d9wtzmp=m0^47^1ivsgem#8ju@'
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    STATIC_ROOT = ''


class Prod(Base):
    SECRET_KEY = values.SecretValue()
    DEBUG = False
    ALLOWED_HOSTS = ['gitview.fvds.ru']
    STATIC_ROOT = values.Value(environ_name='STATIC_ROOT')
