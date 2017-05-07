from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from FoodieApp.forms import UserForm
from FoodieApp.tests.test_base import TestBase


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
                                data={'email': self.WRONG_EMAIL_FORMAT,
                                      'password': self.DEFAULT_PASSWORD})
        self.assertEqual(200, resp.status_code)
        self.failIf(resp.context['user_form'].is_valid())
