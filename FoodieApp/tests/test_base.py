from django.test import TestCase


class TestBase(TestCase):
    # urls
    SIGNUP_URL = 'cook-signup'
    COOK_HOME_URL = 'cook-home'

    # registration info
    DEFAULT_EMIAL = 'test@example.com'
    DEFAULT_PASSWORD = 'password'
    WRONG_EMAIL_FORMAT = 'test'
