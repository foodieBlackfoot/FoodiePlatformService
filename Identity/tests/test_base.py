import os
from PIL import Image
from io import BytesIO

from django.core.files.base import File
from django.test import TestCase
from django.urls import reverse

from FoodieService import settings


class TestBase(TestCase):
    # urls
    SIGNUP_URL = 'cook-signup'
    SIGNIN_URL = 'cook-sign-in'
    SIGNOUT_URL = 'cook-sign-out'

    COOK_HOME_URL = 'cook-home'
    COOK_APPLY_URL = 'apply'
    COOK_ACCOUNT_URL = 'cook-account'
    COOK_MENU_URL = 'cook-menu'
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
    DEFAULT_LOGO_NAME = 'test.png'

    # fields
    FIELD_EMAIL = 'email'
    FIELD_PASSWORD = 'password'
    FIELD_NAME = 'Name'
    FIELD_DESC = 'Description'
    FIELD_TAG = 'Tag'
    FIELD_ADDRESS = 'Address'
    FIELD_PHONE = 'Phone'
    FIELD_LOGO = 'Logo'
    FIELD_AVATAR = 'Avatar'

    # Sign up for a new user
    def signup_new_user(self):
        self.client.post(reverse(self.SIGNUP_URL),
                         data={self.FIELD_EMAIL: self.DEFAULT_EMIAL,
                               self.FIELD_PASSWORD: self.DEFAULT_PASSWORD})

    # Log in with valid user
    def user_login(self):
        self.client.login(username=self.DEFAULT_EMIAL,
                          password=self.DEFAULT_PASSWORD)

    # Become a cook
    def apply_cook(self):
        with open(self.DEFAULT_LOGO, 'rb') as logo:
            self.client.post(reverse(self.COOK_APPLY_URL),
                             data={self.FIELD_NAME: self.DEFAULT_NAME,
                                   self.FIELD_DESC: self.DEFAULT_DESC,
                                   self.FIELD_TAG: self.DEFAULT_TAG,
                                   self.FIELD_ADDRESS: self.DEFAULT_ADDRESS,
                                   self.FIELD_PHONE: self.DEFAULT_PHONE_NUMBER,
                                   self.FIELD_LOGO: logo})

    def get_logo_file(self, ext='png', size=(50, 50), color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=self.DEFAULT_LOGO_NAME)

    def delete_logo_file(self):
        name = os.path.join(settings.MEDIA_ROOT+settings.COOK_LOGO_ROOT,
                            self.DEFAULT_LOGO_NAME)
        os.remove(name)
