from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class SoftUserManager(UserManager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class User(AbstractUser):
    mobile = models.CharField(_("mobile"), max_length=11, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    deleted = models.BooleanField(default=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(_("is email verified"), default=False)

    objects = SoftUserManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()




