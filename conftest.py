INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',

    'sudo',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]


def pytest_report_header(config):
    return 'made with love: <3'


def pytest_configure(config):
    from django.conf import settings

    settings.configure(
        AUTHENTICATION_BACKENDS=[
            'tests.base.FooPasswordBackend',
            'tests.base.StubPasswordBackend',
        ],
        DEBUG=True,
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'NAME': ':memory:',
                'ENGINE': 'django.db.backends.sqlite3',
                'TEST_NAME': ':memory:',
            },
        },
        DATABASE_NAME=':memory:',
        TEST_DATABASE_NAME=':memory:',
        INSTALLED_APPS=INSTALLED_APPS,
        MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,
        PASSWORD_HASHERS=['django.contrib.auth.hashers.MD5PasswordHasher'],
        ROOT_URLCONF='tests.urls',
    )
