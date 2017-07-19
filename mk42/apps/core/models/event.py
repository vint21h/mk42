# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/event.py


from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


from redactor.fields import RedactorField



__all__ = [
    "Event",
]


class Event(models.Model):
    """
    Event model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    name = models.CharField(verbose_name=_("name"), max_length=256, db_index=True, unique=True)
    description = RedactorField(verbose_name=_("description"), blank=True, null=True, db_index=True)
    group = models.ForeignKey("core.Group", verbose_name=_("group"), db_index=True, related_name="events")
    address = models.CharField(verbose_name=_("address"), max_length=2048, blank=False, null=True, db_index=True)
    start = models.DateTimeField(verbose_name=_("start date/time"), blank=False, null=True, db_index=True)
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("start date/time"), blank=True, null=True, db_index=True, auto_now=True)


    class Meta:

        unique_together = ["group", "start",]
        app_label = "core"
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["-created", "-start"]

    def __unicode__(self):

        return self.name

    def __str__(self):

        return self.__unicode__()


