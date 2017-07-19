# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/rsvp.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


__all__ = [
    "RSVP",
]


class RSVP(models.Model):
    """
    RSVP (Répondez s'il vous plaît) model.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_("ID"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("user"), db_index=True, related_name="rsvp")
    event = models.ForeignKey("core.Event",  verbose_name=_("event"), db_index=True, related_name="rsvp")
    created = models.DateTimeField(verbose_name=_("created date/time"), blank=True, null=True, db_index=True, auto_now_add=True)


    class Meta:

        app_label = "core"
        verbose_name = _("rsvp")
        verbose_name_plural = _("rsvp")
        ordering = ["-created", ]

    def __unicode__(self):

        return "{user}: {event}".format(**{
            "user": self.user,
            "event": self.event,
        })

    def __str__(self):

        return self.__unicode__()
