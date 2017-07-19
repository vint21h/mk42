# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/signals/group.py

from __future__ import unicode_literals

from mk42.apps.core.models.membership import Membership


__all__ = [
    "post_save_group",
]


def post_save_group(sender, instance, created, **kwargs):
    """
    Create group membership for group owner.

    :param sender: sender model class.
    :type sender: object.
    :param instance: group model instance.
    :type instance: mk42.apps.core.models.group.Group.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    """

    if created:

        Membership.objects.get_or_create(user=instance.owner, group=instance, active=True)
