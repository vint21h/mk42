# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/group.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save

from autoslug import AutoSlugField
from redactor.fields import RedactorField

from mk42.apps.core.managers.group import GroupManager
from mk42.apps.core.signals.group import post_save_group


__all__ = [
    "Group",
]


class Group(models.Model):
    """
    Group model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True, unique=True)
    slug = AutoSlugField(verbose_name=_("slug"), populate_from="name", max_length=256, default="", blank=True, db_index=True, editable=True, help_text=_("overwrites during creation"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("owner"), db_index=True, related_name="owned")
    description = RedactorField(verbose_name=_("description"), blank=True, null=True, db_index=True)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated date/time"), blank=True, null=True, db_index=True, auto_now=True)
    active = models.BooleanField(verbose_name=_("active"), db_index=True, default=True)

    objects = GroupManager()

    class Meta:

        app_label = "core"
        verbose_name = _("group")
        verbose_name_plural = _("groups")
        ordering = ["-created", ]

    def __unicode__(self):

        return self.name

    def __str__(self):

        return self.__unicode__()

    def send_create_group_email(self):
        """
        Send the notification email to the user after creating a group.
        """

        self.owner.send_email("create_group_email", {"group": self, })


# register signals
post_save.connect(post_save_group, sender=Group)
