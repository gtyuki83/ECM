from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Users(models.Model):

    user_name = models.CharField(
        _('user_name'), max_length=128, null=False, blank=False)
    mail_address = models.CharField(
        _('mail_address'), max_length=128, null=False, blank=False)
    created = models.DateTimeField(_('created'), default=timezone.now)


class Schedules(models.Model):

    schedule_date = models.DateField(
        _('schedule_date'), null=False, blank=False)

    user_name = models.CharField(
        _('user_name'), max_length=128, null=False, blank=False
    )
    schedule = models.CharField(
        _('schedule'), max_length=128, null=False, blank=False
    )
    remark = models.TextField(_('remark'), null=False, blank=False)
