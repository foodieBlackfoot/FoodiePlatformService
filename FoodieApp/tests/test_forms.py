from django.core.files.uploadedfile import SimpleUploadedFile

from FoodieApp.forms import UserForm, CookForm, CustomerForm
from FoodieApp.tests.test_base import TestBase


class UserFormTests(TestBase):
    """
    Test user related forms: UserForm, CookForm, CustomerForm
    
    """

    INVALID_MESSAGE = 'This field is required.'

    # User Form
    def test_user_valid(self):
        user_data = {self.FIELD_EMAIL: self.DEFAULT_EMIAL,
                     self.FIELD_PASSWORD: self.DEFAULT_PASSWORD}
        user_form = UserForm(data=user_data)
        saved_user = user_form.save()

        self.assertTrue(user_form.is_valid())
        self.assertEqual(saved_user.email, self.DEFAULT_EMIAL)
        self.assertEqual(saved_user.password, self.DEFAULT_PASSWORD)

    def test_user_blank(self):
        user_form = UserForm({})

        self.assertFalse(user_form.is_valid())
        self.assertEqual(user_form.errors, {
            self.FIELD_EMAIL: [self.INVALID_MESSAGE],
            self.FIELD_PASSWORD: [self.INVALID_MESSAGE]
        })

    # Cook Form
    def test_cook_valid(self):
        upload_file = open(self.DEFAULT_LOGO, 'rb')
        post_dict = {self.FIELD_NAME: self.DEFAULT_NAME,
                     self.FIELD_DESC: self.DEFAULT_DESC,
                     self.FIELD_TAG: self.DEFAULT_TAG,
                     self.FIELD_ADDRESS: self.DEFAULT_ADDRESS,
                     self.FIELD_PHONE: self.DEFAULT_PHONE_NUMBER}
        file_dict = {self.FIELD_LOGO: SimpleUploadedFile(upload_file.name,
                                                upload_file.read())}
        cook_form = CookForm(post_dict, file_dict)
        saved_cook = cook_form.save(commit=False)

        self.assertTrue(cook_form.is_valid())
        self.assertEqual(saved_cook.Name, self.DEFAULT_NAME)
        self.assertEqual(saved_cook.Description, self.DEFAULT_DESC)
        self.assertEqual(saved_cook.Tag, self.DEFAULT_TAG)
        self.assertEqual(saved_cook.Address, self.DEFAULT_ADDRESS)
        self.assertEqual(saved_cook.Phone, self.DEFAULT_PHONE_NUMBER)
        self.assertIsNotNone(saved_cook.Logo)

    def test_cook_invalid(self):
        cook_form = CookForm({})

        self.assertFalse(cook_form.is_valid())
        self.assertEqual(cook_form.errors, {
            self.FIELD_NAME: [self.INVALID_MESSAGE],
            self.FIELD_DESC: [self.INVALID_MESSAGE],
            self.FIELD_TAG: [self.INVALID_MESSAGE],
            self.FIELD_ADDRESS: [self.INVALID_MESSAGE],
            self.FIELD_PHONE: [self.INVALID_MESSAGE],
            self.FIELD_LOGO: [self.INVALID_MESSAGE]
        })

    # Customer
    def test_customer_blank(self):
        customer_data = {self.FIELD_AVATAR: self.DEFAULT_LOGO,
                         self.FIELD_PHONE: self.DEFAULT_PHONE_NUMBER,
                         self.FIELD_ADDRESS: self.DEFAULT_ADDRESS}

        customer_form = CustomerForm(data=customer_data)
        saved_customer = customer_form.save(commit=False)

        self.assertTrue(customer_form.is_valid())
        self.assertEqual(saved_customer.Avatar, self.DEFAULT_LOGO)
        self.assertEqual(saved_customer.Phone, self.DEFAULT_PHONE_NUMBER)
        self.assertEqual(saved_customer.Address, self.DEFAULT_ADDRESS)

    def test_customer_blank(self):
        customer_form = CustomerForm({})

        self.assertFalse(customer_form.is_valid())
        self.assertEqual(customer_form.errors, {
            self.FIELD_AVATAR: [self.INVALID_MESSAGE],
            self.FIELD_PHONE: [self.INVALID_MESSAGE],
            self.FIELD_ADDRESS: [self.INVALID_MESSAGE]
        })