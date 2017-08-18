# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/models/membership.py

from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save

from mk42.apps.core.managers.membership import MembershipManager
from mk42.apps.core.signals.membership import post_save_membership


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

    def save(self, *args, **kwargs):
        """
        Save and send notification.
        """

        old = Membership.objects.get(pk=self.pk)

        if all([self.active, self.active != old.active, ]):

            self.send_membership_approve_email()

        super(Membership, self).save(*args, **kwargs)

    def send_membership_creation_email(self):
        """
        Send the notification email to the user after request membership to the group.
        """

        self.user.send_email("membership_creation", {"membership": self, })

    def send_membership_approve_email(self):
        """
        Send the notification email to the user after approving request membership to the group.
        """

        if self.active:

            self.user.send_email("membership_approve", {"membership": self, })

# register signals
post_save.connect(post_save_membership, sender=Membership)
