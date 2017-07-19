# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/managers/membership.py

from __future__ import unicode_literals

from django.db import models

from mk42.apps.core.querysets.membership import MembershipQuerySet


__all__ = [
    "MembershipManager",
]


class MembershipManager(models.Manager):
    """
    Membership model manager.
    """

    def get_queryset(self):
        """
        Override to return custom queryset.

        :return: Membership model queryset instance.
        :rtype: mk42.apps.core.querysets.membership.MembershipQuerySet.
        """

        return MembershipQuerySet(self.model, using=self._db)

    def active(self, *args, **kwargs):
        """
        Return active memberships.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with active memberships.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().active(*args, **kwargs)

    def inactive(self, *args, **kwargs):
        """
        Return inactive memberships.

        :param args: additional args.
        :type args: list.
        :param kwargs: additional args.
        :type kwargs: dict.
        :return: queryset with inactive memberships.
        :rtype: django.db.models.query.QuerySet.
        """

        return self.get_queryset().inactive(*args, **kwargs)
