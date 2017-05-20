from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from Identity.forms import UserForm
from Identity.models import Cook
from Identity.tests.test_base import TestBase


class DefaultRegistrationTests(TestBase):
    """
        Test the default registration backend.

    """

    # default pages
    DEFAULT_SIGNUP_PAGE = 'base_signup.html'

    def test_registration_get(self):
        """
        HTTP ``GET`` to the signup view uses the appropriate
        template and populates a signup form into the context.
        """

        resp = self.client.get(reverse(self.SIGNUP_URL))
        self.assertEqual(200, resp.status_code)
        self.assertTemplateUsed(resp, self.DEFAULT_SIGNUP_PAGE)
        self.failUnless(isinstance(resp.context['user_form'], UserForm))

    def test_signup_happycase(self):
        resp = self.client.post(reverse(self.SIGNUP_URL),
                                data={'email': self.DEFAULT_EMIAL,
                                      'password': self.DEFAULT_PASSWORD})

        self.assertRedirects(resp, reverse(self.COOK_HOME_URL))

        new_user = get_user_model().objects.get(email=self.DEFAULT_EMIAL)
        self.failUnless(new_user.check_password(self.DEFAULT_PASSWORD))

    def test_signup_wrong_email_fail(self):
        resp = self.client.post(reverse(self.SIGNUP_URL),
                                data={self.FIELD_EMAIL: self.WRONG_EMAIL_FORMAT,
                                      self.FIELD_PASSWORD: self.DEFAULT_PASSWORD})
        self.assertEqual(200, resp.status_code)
        self.failIf(resp.context['user_form'].is_valid())

    def test_signin_happycase(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.SIGNIN_URL))
        self.assertEquals(resp.status_code, 200)

        islogin = self.client.login(username=self.DEFAULT_EMIAL,
                                    password=self.DEFAULT_PASSWORD)
        self.assertTrue(islogin)

    def test_signin_wrong_password(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.SIGNIN_URL))
        self.assertEquals(resp.status_code, 200)

        islogin = self.client.login(username=self.DEFAULT_EMIAL,
                                    password="wrongpassword")
        self.assertFalse(islogin)

    def test_signin_wrong_email(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.SIGNIN_URL))
        self.assertEquals(resp.status_code, 200)

        islogin = self.client.login(username="wrong_email@wrong.com",
                                    password=self.DEFAULT_PASSWORD)
        self.assertFalse(islogin)

    def test_logout(self):
        self.signup_new_user()
        self.user_login()

        resp = self.client.get(reverse(self.SIGNOUT_URL))
        self.assertEquals(resp.status_code, 302)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_HOME_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/')

    def test_cook_home_page(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOK_HOME_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_HOME_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/')

    def test_cook_apply_page_availability(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOK_APPLY_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_APPLY_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/apply/')

    def test_cook_apply_page(self):
        self.signup_new_user()

        with open(self.DEFAULT_LOGO, 'rb') as logo:
            resp = self.client.post(reverse(self.COOK_APPLY_URL),
                                    data={self.FIELD_NAME: self.DEFAULT_NAME,
                                          self.FIELD_DESC: self.DEFAULT_DESC,
                                          self.FIELD_TAG: self.DEFAULT_TAG,
                                          self.FIELD_ADDRESS: self.DEFAULT_ADDRESS,
                                          self.FIELD_PHONE: self.DEFAULT_PHONE_NUMBER,
                                          self.FIELD_LOGO: logo})
        self.assertRedirects(resp, reverse(self.COOK_HOME_URL))

        new_cook = Cook.objects.get(Name=self.DEFAULT_NAME)
        self.assertEqual(new_cook.Description, self.DEFAULT_DESC)
        self.assertEqual(new_cook.Tag, self.DEFAULT_TAG)
        self.assertEqual(new_cook.Address, self.DEFAULT_ADDRESS)
        self.assertEqual(new_cook.Phone, self.DEFAULT_PHONE_NUMBER)

        self.delete_logo_file()

    def test_cook_account_page(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOK_ACCOUNT_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_ACCOUNT_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/account/')

    def test_cook_meal_page(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOK_MEAL_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_MEAL_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/meal/')

    def test_cook_order_page(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOK_ORDER_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOK_ORDER_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/order/')

    def test_cook_report_page(self):
        self.signup_new_user()

        resp = self.client.get(reverse(self.COOD_REPORT_URL))
        self.assertEquals(resp.status_code, 200)

        self.client.logout()

        resp = self.client.get(reverse(self.COOD_REPORT_URL))
        self.assertRedirects(resp, '/cook/sign-in/?next=/cook/report/')

    # Sign up for a new user
    def signup_new_user(self):
        self.client.post(reverse(self.SIGNUP_URL),
                         data={self.FIELD_EMAIL: self.DEFAULT_EMIAL,
                               self.FIELD_PASSWORD: self.DEFAULT_PASSWORD})

    # Log in with valid user
    def user_login(self):
        self.client.login(username=self.DEFAULT_EMIAL,
                          password=self.DEFAULT_PASSWORD)
