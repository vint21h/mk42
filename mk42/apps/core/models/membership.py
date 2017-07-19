# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/membership.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from mk42.apps.core.managers.membership import MembershipManager


__all__ = [
    "Membership",
]


class Membership(models.Model):
    """
    Membership model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), db_index=True, related_name="membership")
    group = models.ForeignKey("core.Group", verbose_name=_("group"), db_index=True, related_name="members")
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)
    active = models.BooleanField(verbose_name=_("active"), db_index=True, default=False)

    objects = MembershipManager()

    class Meta:

        app_label = "core"
        verbose_name = _("membership")
        verbose_name_plural = _("membership")
        ordering = ["-created", ]

    def __unicode__(self):

        return "{user}: {group}".format(**{
            "user": self.user,
            "group": self.group,
        })

    def __str__(self):

        return self.__unicode__()
