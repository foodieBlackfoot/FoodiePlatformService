from django.contrib.auth import get_user_model

from Identity.tests.test_base import TestBase
from Identity.models import Cook, Customer


class UserModelsTests(TestBase):
    """
        Test user related models: User, Cook, Customer

    """
    DEFAULT_FIRST_NAME = "first_name"
    DEFAULT_LAST_NAME = "last_name"
    DEFAULT_RATING = "rating"

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, get_user_model()))

    def test_cook_creation(self):
        user = self.create_user()
        cook = self.create_cook(user)
        self.assertTrue(isinstance(cook, Cook))
        self.assertEqual(cook.__str__(), cook.Name)
        self.delete_logo_file()

    def test_customer_creation(self):
        user = self.create_user()
        customer = self.create_customer(user)
        self.assertTrue(isinstance(customer, Customer))
        self.assertEqual(customer.__str__(), customer.User.get_full_name())

    # Helpers
    def create_user(self):
        return get_user_model().objects.create_user(
            email=self.DEFAULT_EMIAL,
            first_name=self.DEFAULT_FIRST_NAME,
            last_name=self.DEFAULT_LAST_NAME,
            is_active=False,
            avatar=self.DEFAULT_LOGO)

    def create_cook(self, user):
        mocked_image = self.get_logo_file()
        return Cook.objects.create(
            User=user,
            Name=self.DEFAULT_NAME,
            Description=self.DEFAULT_DESC,
            Rating=self.DEFAULT_RATING,
            Tag=self.DEFAULT_TAG,
            Address=self.DEFAULT_ADDRESS,
            Phone=self.DEFAULT_PHONE_NUMBER,
            Logo=mocked_image
        )

    def create_customer(self, user):
        return Customer.objects.create(
            User=user,
            Phone=self.DEFAULT_PHONE_NUMBER,
            Address=self.DEFAULT_ADDRESS,
            Avatar=self.DEFAULT_LOGO,
        )