from django.test import TestCase


class TestBase(TestCase):
    # urls
    SIGNUP_URL = 'cook-signup'
    SIGNIN_URL = 'cook-sign-in'
    SIGNOUT_URL = 'cook-sign-out'

    COOK_HOME_URL = 'cook-home'
    COOK_APPLY_URL = 'apply'
    COOK_ACCOUNT_URL = 'cook-account'
    COOK_MEAL_URL = 'cook-meal'
    COOK_ORDER_URL = 'cook-order'
    COOD_REPORT_URL = 'cook-report'

    # registration info
    DEFAULT_EMIAL = 'test@example.com'
    DEFAULT_PASSWORD = 'password'
    WRONG_EMAIL_FORMAT = 'test'

    # cook application info
    DEFAULT_NAME = 'BOB HANK'
    DEFAULT_DESC = 'good'
    DEFAULT_TAG = 'Sushi'
    DEFAULT_ADDRESS = '123 ABC St. Seattle WA 98121'
    DEFAULT_PHONE_NUMBER = '1234567890'
    DEFAULT_LOGO = 'test_resources/test_images/test.png'
