from PIL import Image
from io import BytesIO

from django.core.files.base import File
from django.contrib.auth import get_user_model

from FoodieApp.tests.test_base import TestBase
from FoodieApp.models import Cook, Customer


class UserModelsTests(TestBase):
    """
        Test user related models: User, Cook, Customer

    """

    def test_user_creation(self):
        user = self.create_user()
        self.assertTrue(isinstance(user, get_user_model()))

    def test_cook_creation(self):
        user = self.create_user()
        cook = self.create_cook(user)
        self.assertTrue(isinstance(cook, Cook))
        self.assertEqual(cook.__str__(), cook.Name)

    def test_customer_createion(self):
        user = self.create_user()
        customer = self.create_customer(user)
        self.assertTrue(isinstance(customer, Customer))
        self.assertEqual(customer.__str__(), customer.User.get_full_name())

    # Helpers
    def create_user(self):
        return get_user_model().objects.create_user(
            email=self.DEFAULT_EMIAL,
            first_name="first_name",
            last_name="last_name",
            is_active=False,
            avatar="avatar_path")

    def create_cook(self, user):
        mocked_image = self.get_image_file()
        return Cook.objects.create(
            User=user,
            Name="name",
            Description="description",
            Rating='rating',
            Tag="tag",
            Address="address",
            Phone="phone",
            Logo=mocked_image
        )

    @staticmethod
    def create_customer(user):
        return Customer.objects.create(
            User=user,
            Avatar="avatar",
            Phone="phone",
            Address="address"
        )

    @staticmethod
    def get_image_file(name='test.png', ext='png', size=(50, 50),
                       color=(256, 0, 0)):
        file_obj = BytesIO()
        image = Image.new("RGBA", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)
