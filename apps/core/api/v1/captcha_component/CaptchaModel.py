# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from config.settings import CAPTCHA_MIN_EXPIRATION

from django.contrib.auth.models import User


def calcular_expiration_time():
    return timezone.now() + timezone.timedelta(minutes=CAPTCHA_MIN_EXPIRATION)


class Captcha(models.Model):
    active = models.BooleanField(default=True, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False, auto_now=True)
    expiration_date = models.DateTimeField(null=False, blank=False, default=calcular_expiration_time)
    uuid = models.CharField(max_length=250, null=False, blank=False, unique=True)
    pass_captcha = models.BooleanField(default=False, null=False, blank=False)
    captcha_text = models.TextField(null=False, blank=False, max_length=10)
    application = models.ForeignKey(User, on_delete=models.CASCADE, related_name='aplication', null=True)

    def __str__(self):
        return 'captcha_id: {} - active: {}'.format(self.id, self.active)

    class Meta:
        indexes = [
            models.Index(fields=['uuid'], name='uuid_idx'),
        ]
        verbose_name = _('Captcha')
        verbose_name_plural = _('Captchas')
        app_label = "core"
        ordering = ['-date', '-id']
