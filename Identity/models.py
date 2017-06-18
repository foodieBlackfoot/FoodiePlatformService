from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from .managers import UserManager


# Cook Model
class Cook(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='cook')
    Name = models.CharField(max_length=500)
    Description = models.CharField(max_length=500)
    Rating = models.CharField(max_length=500, null=True)
    Tag = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Logo = models.ImageField(upload_to=settings.COOK_LOGO_ROOT, blank=False)

    def __str__(self):
        return self.Name


# Customer Model
class Customer(models.Model):
    User = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='customer')
    Avatar = models.CharField(max_length=500)
    Phone = models.CharField(max_length=500)
    Address = models.CharField(max_length=500)

    def __str__(self):
        return self.User.get_full_name()


# Customize User to use email as auth token
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def get_avatar(self):
        """
        Returns the path to the avatar
        """
        return self.avatar

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
