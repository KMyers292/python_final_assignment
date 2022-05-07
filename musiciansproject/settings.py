"""
Django settings for musiciansproject project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rnfkejktxiz3r(e=qu)*u0p%@5z%1a&0-il%=xmk4&=q(aho&3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# Once our model has been created we need to add our app to the list of installed apps which is in the settings.py file.
# This is done by accessing the MusiciansConfig class which is stored in the apps module.
INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'musicians.apps.MusiciansConfig',
    'albums.apps.AlbumsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'musiciansproject.urls'

# Like Jinja, all Django tempaltes are saved in a folder called templates by convention.
# Django will automatically look for template files for each app listed in the INSTALLED_APPS variable in a folder with the name /templates within that app's directory.
# You can also list any additional template files directories by adding to the 'DIRS' key of the TEMPLATES variable.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # The BASE_DIR variable points to the root directory of your project and can be combined with other paths.
            # This variable is not provided by default and MUST be added for Django to find template files in the musiciansproject folder.
            BASE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # For Django templates to find media, it is also necessary to add a media context processor to the list of context processors which is stored in the TEMPLATES variable in the settings.py file.
                'django.template.context_processors.media',
                # The above list item is not provided by default and must be added for Django templates to find uploaded media!
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'musiciansproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Change the DB settings to the following to connect to connect to PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'musicians',
        'USER': 'postgres',
        'PASSWORD': 'postgres', # Whatever you set it to during the setup
        'HOST': '::1',
        'PORT': '5433', # Most likely 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# All unchanging, static assets such as CSS files, JavaScript files and image files should be saved in a folder called /static.
# By default Django will automatically look for static files for each app listed in the INSTALLED_APPS variable in a folder with the name /static within that app's directory. You could change the name of this path to use a different folder name or structure for static assets by altering this variable.
STATIC_URL = '/static/'

# You can also list any additonal static files directories by adding the STATICFILES_DIRS variable to the settings.py file and setting it to a lisst of paths to static files directories.
# This is useful if you want to include static files which are used accross the whole project.
# This variable is not provided by default and MUST be added for Django to find static files in the musiciansproject directory.

STATICFILES_DIRS = [
    BASE_DIR / 'musiciansproject/static'
]

# All uploaded media such as image and audio files should be saved in a folder called /media which should be located in the root directory of hte project folder (in our case).
# It is necessary to specify where the folder is by adding this code in our settings.py file.
# This is not provided by default and must be added for Django's development server to find the uploaded media files.
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# By default, Django provides a pre-written fully functional User model which can be used to create new users.
# However, the recommended practice is to create a custom user model class as a child of the existing User model class as soon as you start a new project in case you want to make any changes to the user model.
# Doing so once you are far into the development of your project especially if the application is live can be very difficult.

# In order for Django to recognizee our custom user model, we need to specify it as the value of the AUTH_USER_MODEL variable in the settings.py file.
AUTH_USER_MODEL = 'users.CustomUser'

# We also need to specify where Django should redirect to when the user logs in or out. To do so, we specify values for the LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL variables.
# We will be creating a welcome page as the home page which the user can be redirected to.
# This is not provided by default and MUST be added for Django to know where to redirect to.
LOGIN_REDIRECT_URL = 'welcome'
LOGOUT_REDIRECT_URL = 'welcome'

# When a user asks to reset their password they would be sent an email with a unique URL which would bring them to a page whre they can reset their password.
# The process of setting up an email server would be complex and would be different depending on which hosting providor you are using.
# To keep things simpler, we will simply save the emails as TXT files in our project directory.
# To do so, we need to set the EMAIL_BACKEND variable to use a file based backend and we need to set the EMAIL_FILE_PATH variable to specify the directory where the files should be saved.
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
