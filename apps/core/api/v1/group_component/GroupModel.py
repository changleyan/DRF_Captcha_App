# -*- coding: utf-8 -*-
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _


class Groupp(Group):

    class Meta:
        proxy = True
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        permissions = (
            ("list_group", "Can list groups"),
        )
