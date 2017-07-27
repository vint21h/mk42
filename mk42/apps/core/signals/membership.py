# -*- coding: utf-8 -*-

# mk42
# mk42/apps/core/signals/membership.py

from __future__ import unicode_literals


__all__ = [
    "post_save_membership",
]


def post_save_membership(sender, instance, created, **kwargs):
    """
    end the notification email to the user after request membership to the group.

    :param sender: sender model class.
    :type sender: object.
    :param instance: membership model instance.
    :type instance: mk42.apps.core.models.membership.Membership.
    :param created: is model instance created/edited.
    :type created: bool
    :param kwargs: additional args.
    :type kwargs: dict.
    """

    if created:

        instance.send_request_membership_email()